#!/bin/python3

import os
import pandas as pd
import fnmatch

# Define the base directory containing subdirectories with CSV files
base_dir = input("Provide base directory: ")  # Example: /path/to/base_directory

# Create a new directory for storing merged CSV files
output_dir = os.path.join(base_dir, "merged_csvs")
os.makedirs(output_dir, exist_ok=True)

# Unique starting patterns for specific files
starting_patterns = [
 "Communicable immunizable*",
    "Communicable non-immunizable*",
    "Injuries and Others*",
    "Mental Health Conditions*",
    " Non-Communicable*",
    " Obstetrics & Gynaecological*",
    " Reproductive Tract*",
    "Specialized Conditions*"
]

# Initialize an empty dictionary to store merged dataframes by type
merged_dfs = {pattern: pd.DataFrame() for pattern in starting_patterns}

# Iterate through each subdirectory in the base directory
for subdir in os.listdir(base_dir):
    subdir_path = os.path.join(base_dir, subdir)
    
    # Check if it's a directory and not a file
    if os.path.isdir(subdir_path):
        # Iterate through each starting pattern
        for pattern in starting_patterns:
            # Glob all CSV files matching the current pattern in the current subdirectory
            pattern_files = fnmatch.filter(os.listdir(subdir_path), pattern)
            
            # Process each file matching the current pattern in the current subdirectory
            for file in pattern_files:
                file_path = os.path.join(subdir_path, file)
                
                # Read the CSV file into a dataframe
                df_specific = pd.read_csv(file_path)
                
                # Append dataframe to the corresponding entry in merged_dfs
                merged_dfs[pattern] = pd.concat([merged_dfs[pattern], df_specific], ignore_index=True)

# Process and save each merged dataframe
for pattern, merged_df in merged_dfs.items():
    # Check if the dataframe is not empty
    if not merged_df.empty:
        # Group by 'Data element' and aggregate numerical columns
        numerical_columns = merged_df.columns.difference(['Data element'])  # Exclude 'Data element' column
        merged_df = merged_df.groupby('Data element')[numerical_columns].sum().reset_index()

        # Write merged dataframe to CSV file in the output directory
        output_filename = os.path.join(output_dir, f"merged_{pattern.split('*')[0]}.csv")
        merged_df.to_csv(output_filename, index=False)
        print(f"Merged and aggregated CSV for {pattern} saved as {output_filename}.")

print(f"All merged and aggregated CSV files saved in {output_dir}.")


