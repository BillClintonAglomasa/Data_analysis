#!/bin/python3

# Import modules
import pandas as pd
#import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Import data
data_path = "/home/aglomasa/Newsletter/Codes/All_diseases_Newsletter/Trial/merged_csvs/Top_10_All_diseases.csv"

# Read data
data = pd.read_csv(data_path)
print(data.columns)
# Select columns
selected_columns = data[["1-11mths", "1-4", "10-14", "15-17", "18-19", "20-34", 
                         "35-49", "5-9", "50-59", "60-69", "70+", "<28days"
]]

# Calculate column totals
column_totals = selected_columns.sum()

# Get columns with the highest and lowest
age_group_highest = column_totals.idxmax()
age_group_lowest = column_totals.idxmin()


# List of columns to be plotted
value_columns_gender = ["Female", "Male  "]
value_columns_age = [age_group_highest, age_group_lowest]

# Define color mapping for consistent colors
color_map = {"Hypertension": "rgb(255, 127, 14)",
    "AUTI": "rgb(44, 160, 44)",
    "Typhoid Fever": "rgb(214, 39, 40)",
    "Malaria": "rgb(148, 103, 189)",
    "URTI": "rgb(140, 86, 75)",
    "Anaemia": "rgb(227, 119, 194)",
    "Ulcer": "rgb(127, 127, 127)",
    "ROA": "rgb(188, 189, 34)",
    "PRC": "rgb(23, 190, 207)",
    "Skin Diseases": "rgb(31, 119, 180)"
}

# Donut plot for gender 
# Initialize the subplot figure with two rows and one column
gender_pie = make_subplots(rows = 2, cols = 1, 
                           specs=[[{"type": "pie"}], [{"type": "pie"}]], 
                           vertical_spacing = 0.3
)

# Loop through each column and create a pie chart
for i, column in enumerate(value_columns_gender):
    # Filter the DataFrame to exclude zero values in the current column
    df_filtered = data[data[column] != 0]

    # Get consistent colors for each label present in the filtered data
    colors = [color_map[label] for label in df_filtered["Data element"]]

    # Add the pie chart to the correct row (1 for Female, 2 for Male)
    gender_pie.add_trace(go.Pie(labels = df_filtered["Data element"], 
                                values = df_filtered[column], 
                                hole = 0.55, 
                                textinfo = "label+percent", 
                                insidetextorientation = "radial", 
                                marker = dict(colors = colors)
                         ), 
                         row = i+1, col = 1
    )

# Update layout with annotations
gender_pie.update_layout(
    annotations = [
        dict(text = "<b>Female Diagnosis Patterns in Top 10 Diseases<b>", 
            x = 0.5, y = 1.11, font = dict(size = 16), showarrow = False
        ),
        dict(text = "<b>Male Diagnosis Patterns in Top 10 Diseases<b>", 
            x = 0.5, y = 0.43, font = dict(size = 16), showarrow = False
        ),
        dict(text = "Female", x = 0.5, y = 0.86, font = dict(size = 20, color = "black"), showarrow = False
        ),
        dict(text = "Male", x = 0.5, y = 0.15, font = dict(size = 20, color = "black"), showarrow = False
        )
    ],
    showlegend = False,
    height = 600  # Adjust height for better visibility
)

# Show the pie chart
gender_pie.write_image("Gender_pie_chart.png")


# Separated pie chart for age group
# Initialize the subplot figure with two rows and one column
age_pie = make_subplots(rows = 2, cols = 1, 
                           specs = [[{"type": "pie"}], [{"type": "pie"}]], 
                           vertical_spacing = 0.3
)

# Loop through each column and create a pie chart
for i, column in enumerate(value_columns_age):
    # Filter the DataFrame to exclude zero values in the current column
    df_filtered = data[data[column] != 0]

    # Get consistent colors for each label present in the filtered data
    colors = [color_map[label] for label in df_filtered["Data element"]]

    # Add the pie chart to the correct row (1 for Female, 2 for Male)
    age_pie.add_trace(go.Pie(labels = df_filtered["Data element"], 
                             values = df_filtered[column],  
                             textinfo = "label+percent", 
                             insidetextorientation = "radial", 
                             marker = dict(colors=colors)
                     ), 
                     row = i+1, col = 1
    )

# Update layout with annotations
age_pie.update_layout(
    annotations = [
        dict(text = f"<b>Most Affected Age Group ({age_group_highest}): Disease Distribution<b>", 
            x = 0.5, y = 1.11, font = dict(size = 16), showarrow = False
        ),
        dict(text = f"<b>Least Affected Age Group ({age_group_lowest}): Disease Distribution<b>", 
            x = 0.5, y = 0.43, font = dict(size = 16), showarrow = False
        )
    ],
    showlegend = False,
    height = 600  # Adjust height for better visibility
)

# Customize the appearance of the slices
age_pie.update_traces(textinfo = "percent+label", pull = [0.8, 0.6, 0.4, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2])
age_pie.write_image("Age_pie_chart.png")

#the bars are too thick, the background should be changed to white. the lines should be changed to blue
# You need to create a unique axis for the plot
# Bar chart for 
# Create the bar plot
top_10 = go.Figure(data = [
    go.Bar(x = data["Data element"], y = data["Total"])
])

# Customize the layout
top_10.update_layout(
    title="Top 10 Most Diagnosed Disease",
   # xaxis_title = 'Categories',
    #yaxis_title = 'Values',
    template = "ggplot2"
)

# Show the plot
top_10.write_image("Top_10_bar_chart.png")
