import pandas as pd
import os

# 1. Set the main folder path where your project is located
folder_path = r"C:\Users\OneDrive\Desktop\group 2

# 2. Define the exact columns required by the assignment rubric
columns = [
    "variable name", "variable label", "definition", "data_type", "unit", 
    "allowed values", "missing value", "source indicator code", 
    "source indicator name", "source", "transformation", "notes"
]

# 3. Enter the detailed information for each variable in the dataset
codebook_data = [
    [
        "Country", "Country Name", "Sovereign state in Sub-Saharan Africa", 
        "String", "None", "List of 47 Sub-Saharan states", "NA", "None", 
        "None", "ILOSTAT Data Explorer", "Filtered from global dataset", 
        "Excludes regional aggregates"
    ],
    [
        "Indicator", "Labour Market Indicator", "Specific labour market metric measured", 
        "String", "None", "Labour force participation, Unemployment, Employment-to-population, Informal employment", 
        "NA", "None", "None", "ILOSTAT Data Explorer", "Merged from 4 separate files", "None"
    ],
    [
        "Sex", "Sex Disaggregation", "Gender category for the observation", 
        "String", "None", "Total, Male, Female", "NA", "None", 
        "None", "ILOSTAT Data Explorer", "None", "None"
    ],
    [
        "Age_Group", "Age Bracket", "Age classification for the observation", 
        "String", "None", "15+, 15-24, 25+, etc.", "NA", "None", 
        "None", "ILOSTAT Data Explorer", "None", "Not present for Informal Employment Rate"
    ],
    [
        "Year", "Reference Year", "Year of observation", 
        "Integer", "Year", "2022", "NA", "None", 
        "None", "ILOSTAT Data Explorer", "Filtered strictly to 2022", 
        "Cross-sectional scope requirement"
    ],
    [
        "Value", "Indicator Value", "Reported numerical value for the indicator", 
        "Decimal", "Percentage", "0-100", "NA", "None", 
        "None", "ILOSTAT Data Explorer", "None", "None"
    ],
    [
        "Observation_Status", "Data Status Flag", "Distinguishes observed data from estimates or models", 
        "String", "None", "Observed, Estimated, Modelled", "NA", "None", 
        "None", "ILOSTAT Data Explorer", "Missing values filled as 'Observed'", "None"
    ]
]

# 4. Create a pandas DataFrame from the lists
df_codebook = pd.DataFrame(codebook_data, columns=columns)

# 5. Create the documentation folder if it does not already exist
docs_folder = os.path.join(folder_path, "documentation")
os.makedirs(docs_folder, exist_ok=True)

# 6. Save the DataFrame to a CSV file
save_path = os.path.join(docs_folder, "codebook.csv")
df_codebook.to_csv(save_path, index=False)

print(f"Success! The codebook has been generated and saved to: {save_path}")
