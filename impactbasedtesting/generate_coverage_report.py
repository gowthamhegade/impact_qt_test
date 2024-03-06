import os
import pandas as pd

def extract_tags(bdd_feature_directory):
    extracted_test_tags = []
    def extract_text(raw_input):
        to_include = False
        #with raw_input:
        for line in raw_input.splitlines():
            if line.startswith('@test'):
                to_include = True
            else:
                to_include = False
        
            if to_include:
                extracted_test_tags.append(line[1:])
                
    for feat_file in os.listdir(bdd_feature_directory):
        if feat_file.endswith('.feature'):
            with open(os.path.join(bdd_feature_directory, feat_file), 'r') as f:
                content = f.read()
                extract_text(content)
    return extracted_test_tags

def process_csv_file(input_csv_file, output_excel_file, Scenario):
    # Read CSV file into a DataFrame
    df = pd.read_csv(input_csv_file, delimiter='\t') 

    # Extract rows between "Function tree" and "Function"
    start_index = df.index[df.iloc[:, 0] == 'Function Tree'].tolist()[0] + 1
    end_index = df.index[df.iloc[:, 0] == 'Functions'].tolist()[0]
    extracted_data = df.iloc[start_index:end_index]

    # Split columns
    # split_columns = extracted_data.iloc[:, 0].str.split(',', expand=True)
    # Use regular expression to split columns while handling commas within quotes
    split_columns = extracted_data.iloc[:, 0].str.split(r',(?=(?:[^"]*"[^"]*")*[^"]*$)', expand=True)

    # Assign new columns to the DataFrame
    extracted_data = pd.concat([extracted_data, split_columns], axis=1)
    extracted_data = extracted_data.iloc[0:, 1:]
    

    # Replace existing column names with values from the first row
    extracted_data.columns = extracted_data.iloc[0]

    # Drop the first row as it's now redundant as column names
    extracted_data = extracted_data[1:]
    extracted_data = extracted_data[1:]
    columns_to_process = ['"Position"', '"Prototype"', '"File"', '"Absolute Path"', '"Executed Instrumentations"',
                         '"Manually Validated Instrumentations"', '"Count of Instrumentations"',
                         '"eLOC - Effective Lines of Code"', '"McCabe - Cyclomatic Complexity"']  

    # Remove double quotes and drop columns for each specified column
    for column in columns_to_process:
        extracted_data[column.replace('"', '')] = extracted_data[column].str.strip('"')
        extracted_data = extracted_data.drop(columns=[column])
    extracted_data['Scenario'] = Scenario
    # Save to Excel file
    extracted_data.to_excel(output_excel_file, index=False)

def process_all_csv_files(data_folder, results_folder):
    # Get a list of all CSV files in the data folder
    csv_files = [file for file in os.listdir(data_folder) if file.endswith('.csv')]

    # Process each CSV file
    for index, test_case in enumerate(csv_files, start=1):
        if not os.path.exists(results_folder):
            os.makedirs(results_folder)

        # Generate input and output file paths
        input_csv_file = os.path.join(data_folder, test_case)
        output_excel_file = os.path.join(results_folder, f'coverage_test{index:03d}.xlsx')

        # Process the CSV file
        process_csv_file(input_csv_file, output_excel_file, 'test' + f'{index:03d}')


# Call the function to process all CSV files
process_all_csv_files(data_folder='data/', results_folder='results/coverage_reports')

def extract_coverage_info(xml_file_path, result_path, scenario_name, mapping=False):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    #file_name_to_class = {}
    class_to_method = {}
    class_coverage_info = {}
    scenario_coverage = {}

    for cl in root.iter('class'):
        class_name = cl.attrib['name']
        file_name = cl.attrib['filename'].split("\\")[-1]

        method = {}
        for method_element in cl.iter('method'):
            method_name = method_element.attrib['name']+method_element.attrib['signature']
            method_name = method_name.split('(')[0]
            if not method_name.startswith('.c'):
                if (class_name,file_name) in class_to_method:
                    class_to_method[(file_name,class_name)].append(method_name)
                else:
                    class_to_method[(file_name,class_name)] = [method_name]
                statements = []
                for lines in method_element.iter('lines'):
                    for statement_element in lines:
                        statements.append((statement_element.attrib['number'],statement_element.attrib['hits']))
                    covered = []
                    if len(statements)>0:
                        for ele in statements:
                            if ele[1] == '1':
                                covered.append(ele[1])
                    if len(covered)>0:
                        coverage_percentage = round(len(covered)*100/len(statements),2)
                        method[method_name] = (coverage_percentage,int(statements[0][0]),int(statements[-1][0])) 
        if method != {}:
            class_coverage_info[(class_name,file_name)] = method

    scenario_coverage[scenario_name] = class_coverage_info  
    df_coverage = pd.DataFrame(data=[(scenario_name,key[0], key[1], subkey, value[0], value[1], value[2]) for key, subdict in scenario_coverage[scenario_name].items() for subkey, value in subdict.items()],columns=['Scenario','Class', 'File_Name', 'Method', 'Coverage_Percentage', 'Start_Line', 'End_Line'])

    with pd.ExcelWriter(os.path.join(result_path,f"coverage_reports\\coverage_{scenario_name}.xlsx")) as w:
        df_coverage.to_excel(w)
    
    if mapping:
        df_class_to_method = pd.DataFrame(data=[(key[0],key[1],method) for key,methods in class_to_method.items() for method in methods],columns=['File_Name','Class_Name','Method'])
        with pd.ExcelWriter(os.path.join(result_path,"class_to_method_mapping.xlsx")) as w:
            df_class_to_method.to_excel(w,index=False)  

