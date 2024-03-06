import os, re
import pandas as pd

def extract_tags(directory_path):
    def remove_prefix(prefix, folders):
        return [folder[len(prefix):] if folder.startswith(prefix) else folder for folder in folders]

    all_items = os.listdir(directory_path)
    folders = [item for item in all_items if os.path.isdir(os.path.join(directory_path, item))]
    pattern = re.compile(r'^tst_')
    selected_folders = [folder for folder in folders if pattern.match(folder)]

    if "tst_":
        selected_folders = remove_prefix("tst_", selected_folders)

    return selected_folders


def process_csv_file(input_csv_file, output_excel_file, Scenario):
    df = pd.read_csv(input_csv_file, delimiter='\t') 
    start_index = df.index[df.iloc[:, 0] == 'Function Tree'].tolist()[0] + 1
    end_index = df.index[df.iloc[:, 0] == 'Functions'].tolist()[0]
    extracted_data = df.iloc[start_index:end_index]

    # Split columns
    # split_columns = extracted_data.iloc[:, 0].str.split(',', expand=True)
    # Use regular expression to split columns while handling commas within quotes
    split_columns = extracted_data.iloc[:, 0].str.split(r',(?=(?:[^"]*"[^"]*")*[^"]*$)', expand=True)
    extracted_data = pd.concat([extracted_data, split_columns], axis=1)
    extracted_data = extracted_data.iloc[0:, 1:]
    extracted_data.columns = extracted_data.iloc[0]


    extracted_data = extracted_data[1:]
    extracted_data = extracted_data[1:]
    columns_to_process = ['"Position"', '"Prototype"', '"File"', '"Absolute Path"', '"Executed Instrumentations"',
                         '"Manually Validated Instrumentations"', '"Count of Instrumentations"',
                         '"eLOC - Effective Lines of Code"', '"McCabe - Cyclomatic Complexity"']  

    for column in columns_to_process:
        extracted_data[column.replace('"', '')] = extracted_data[column].str.strip('"')
        extracted_data = extracted_data.drop(columns=[column])
    extracted_data['Scenario'] = Scenario
    extracted_data.rename(columns={'"Multiple Conditions %"': 'Coverage_Percentage'}, inplace=True)
    extracted_data.rename(columns={'File': 'File_Name'}, inplace=True)
    extracted_data.rename(columns={'Prototype': 'Method'}, inplace=True)

    extracted_data.to_excel(output_excel_file, index=False)

def report_generation(data_folder, results_folder, scenario):

    csv_files = [file for file in os.listdir(data_folder) if file.endswith('.csv')]

    for test_case in csv_files:
        if not os.path.exists(results_folder):
            os.makedirs(results_folder)

        input_csv_file = os.path.join(data_folder, test_case)
        output_excel_file = os.path.join(results_folder, f'coverage_test_{scenario}.xlsx')
        process_csv_file(input_csv_file, output_excel_file, scenario)



report_generation(data_folder='data/', results_folder='results/coverage_reports', scenario = 'LaunchApplication')

