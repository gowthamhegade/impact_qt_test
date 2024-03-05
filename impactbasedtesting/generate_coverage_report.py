import os
import pandas as pd

def process_csv_file(input_csv_file, output_excel_file):
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

    # Save to Excel file
    extracted_data.to_excel(output_excel_file, index=False)

def process_all_csv_files(data_folder, results_folder):
    # Get a list of all CSV files in the data folder
    csv_files = [file for file in os.listdir(data_folder) if file.endswith('.csv')]

    # Process each CSV file
    for test_case in csv_files:
        if not os.path.exists('results'):
            os.makedirs('results')
        # Generate input and output file paths
        input_csv_file = os.path.join(data_folder, test_case)
        output_excel_file = os.path.join(results_folder, f'results_{os.path.splitext(test_case)[0]}.xlsx')

        # Process the CSV file
        process_csv_file(input_csv_file, output_excel_file)

# Call the function to process all CSV files
process_all_csv_files(data_folder='data/', results_folder='results/')

