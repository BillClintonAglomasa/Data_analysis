#!/bin/python3

#class options
#class Import_modules (object):
#
#    def import_modules(self):
#        import os
#        import pandas as pd
        
# load models
# Concate models using unique keys
import os
import pandas as pd

# Define the path where your CSV files are located
base_dir = input("Please provide directory: ")

# Initialize an empty list to store dataframes
dfs = []

# Iterate through each CSV file and read it into a dataframe
for filename in os.listdir(base_dir):
    if filename.endswith(".csv"):
        filepath = os.path.join(base_dir, filename)
        
        # Read the csv file into a Dataframe and append to dfs
        df = pd.read_csv(filepath)
        dfs.append(df)

# Concatenate all dataframes vertically
combined_df = pd.concat(dfs, ignore_index=True)

# List of Data element entries to be removed
exclusions = ["Uncomplicated Malaria Suspected Tested", "Uncomplicated Malaria suspected",
            "Uncomplicated Malaria not tested but treated as malaria",
            "Uncomplicated Malaria Cases Tested Negative but Treated as Malaria",
            "Uncomplicated Malaria in Pregnancy suspected",
            "Uncomplicated Malaria in Pregnancy Suspected Tested",
            "Uncomplicated Malaria in Pregnancy tested positive",
            "Uncomplicated Malaria in Pregnacy not tested but treated as malaria",
            "Uncomplicated Malaria in Pregnancy Tested Negative but Treated as Malaria",
            "Severe Malaria (Non-Lab-Confirmed)"
]

# Remove rows in Data element with the following entries
combined_df = combined_df[~combined_df["Data element"].isin(exclusions)]

# Sort the DataFrame based on the existing 'Total' column
sorted_df = combined_df.sort_values(by="Total", ascending=False)

# Calculate the sum of the total column
sum_total = sorted_df["Total"].sum()

# Create a new column named "Percentage" using the sum of the Total column
sorted_df["Percentage"] = (sorted_df["Total"] / sum_total) * 100
sorted_df["Percentage"] = sorted_df["Percentage"].round(2)

# Drop All other Diseases row and Select top 10 diseases by total infections
sorted_df = sorted_df[sorted_df["Data element"] != "All other Diseases"]
top_10_df = sorted_df.nlargest(10, 'Total')

# Replace multiple values in the "Data element" column
top_10_df["Data element"] = top_10_df["Data element"].replace({"Acute Urinary Tract Infection": "AUTI", "Uncomplicated Malaria Tested Positive ": "Malaria", "Upper Respiratory Tract Infections": "URTI", "Rheumatism / Other Joint Pains / Arthritis": "ROA", "Pregnancy Related Complications": "PRC"})

# Write the combined DataFrame to a new CSV file in the base directory
output_filepath = os.path.join(base_dir, "All_diseases.csv")
output_filepath_top_10 = os.path.join(base_dir, "Top_10_All_diseases.csv")
sorted_df.to_csv(output_filepath, index=False)
print("All_diseases csv created")
top_10_df.to_csv(output_filepath_top_10, index=False)
print("Top_10_All_diseases csv created")
