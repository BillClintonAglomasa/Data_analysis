#!/usr/bin/python3.10

#importing modules
import pandas as pd
import numpy as np
import openpyxl
#import matplotlib.pyplot as plt
#import seaborn as sns
import csv

#path to dataset
PML_case_path = input("Provide path of file")

#reading dataset
PML_case_data = pd.read_csv(PML_case_path)


# Get the number of duplicates before removal
num_duplicates_before = len(PML_case_data) - len(PML_case_data.drop_duplicates(subset=['Title']))

# Remove duplicates based on the "Title" column
PML_case_data_unique_title = PML_case_data.drop_duplicates(subset=['Title'])

# Get the number of duplicates after removal
num_duplicates_after = len(PML_case_data_unique_title) - len(PML_case_data_unique_title.drop_duplicates(subset=['Title']))

# Print the number of duplicates removed
print(f"Number of duplicates removed based on the 'Title' column: {num_duplicates_before - num_duplicates_after}")

PML_case_data_unique_title.to_csv("./Data_without_duplicates.csv")
#Accessing a specific sheet ie month 0
#PML_case_Month_0 = PML_case_data[0]

#Creating a dataframe
#PML_case_Month_0 = pd.DataFrame(PML_case_Month_0)
#PML_case_Month_0.to_csv("../Generated_files/PML_case_Month_0", index = True)

#creating a list of columns from original dataset
#column_list = PML_case_Month_0.columns

#dropping columns without any entry
#PML_case_Month_0_cleaned = PML_case_Month_0.dropna(axis=1, how='all')
#print(PML_case_Month_0_cleaned)

#creating my column list
#column_list = PML_case_Month_0_cleaned.columns

# Count qualitative data for each column
#for column in PML_case_data.columns:
#    counts = PML_case_data[column].value_counts().reset_index()
#    counts.columns = ['Value', 'Count']
#    print(f"Counts for {column}:\n{counts}\n")
    
    #Save counts to a CSV file
#    counts.to_csv(f'{column}_counts.csv', header=['Value', 'Count'])

# Plotting
#specific_sheet_df['Column1'].plot(kind='bar')
