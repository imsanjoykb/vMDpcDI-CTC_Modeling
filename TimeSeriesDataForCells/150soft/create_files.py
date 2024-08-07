import os
import pandas as pd

# Function to read CSV files in numerical order from a directory
def read_csv_files_in_order(directory):
    def extract_number(filename):
        return int(filename.split('.')[1])

    files = sorted([f for f in os.listdir(directory) if f.startswith('PLT.') and f.endswith('.csv')], key=extract_number)
    return files

# Function to create or append to CSV files based on baseCellId value
def split_csv_rows_by_baseCellId(files, input_directory, output_directory):
    for file in files:
        file_path = os.path.join(input_directory, file)
        df = pd.read_csv(file_path)

        for _, row in df.iterrows():
            baseCellId = row['baseCellId']
            output_file = os.path.join(output_directory, f'output_{baseCellId}.csv')
            if not os.path.exists(output_file):
                row.to_frame().T.to_csv(output_file, index=False, mode='w')
            else:
                row.to_frame().T.to_csv(output_file, index=False, mode='a', header=False)

# Get the current working directory
current_directory = os.getcwd()

# Specify the input and output directories
input_directory = current_directory
output_directory = os.path.join(input_directory, 'output')

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Read files in numerical order
files = read_csv_files_in_order(input_directory)

# Split rows into separate CSV files based on baseCellId
split_csv_rows_by_baseCellId(files, input_directory, output_directory)

print(f"CSV files have been processed and split into {output_directory}")
