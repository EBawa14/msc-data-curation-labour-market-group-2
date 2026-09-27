import pandas as pd
import os

# 1. Set the folder where your data is stored
folder_path = r"C:\Users\antwi\OneDrive\Desktop\jones work\group 2"

# 2. Make a list of all the Sub-Saharan African countries
ssa_countries = [
    "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde",
    "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo", 
    "Democratic Republic of the Congo", "Côte d'Ivoire", "Equatorial Guinea", 
    "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", 
    "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Madagascar", "Malawi", 
    "Mali", "Mauritania", "Mauritius", "Mozambique", "Namibia", "Niger", 
    "Nigeria", "Rwanda", "Sao Tome and Principe", "Senegal", "Seychelles", 
    "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Togo", 
    "Uganda", "United Republic of Tanzania", "Zambia", "Zimbabwe"
]

# We use 2022 because the data has more than 20 countries for this year
chosen_year = 2022

# 3. List the exact names of the downloaded Excel files
file_names = [
    "Labour_force_Participation.xlsx",
    "Unemployment Rate.xlsx",
    "Employment_to_Population.xlsx",
    "Informal Employment Rate.xlsx"
]

# This empty list will hold the cleaned data from each file
all_cleaned_data = []

# 4. Loop through each file one by one
for file_name in file_names:
    print("Now working on:", file_name)
    
    # Create the full path to find the file on your computer
    full_path = os.path.join(folder_path, file_name)
    
    # Read the Excel file into a pandas table (DataFrame)
    df = pd.read_excel(full_path)
    
    # Step A: Filter to keep only the rows for the year 2022
    df = df[df['time'] == chosen_year]
    
    # Step B: Filter to keep only the Sub-Saharan African countries
    df = df[df['ref_area.label'].isin(ssa_countries)]
    
    # Step C: Select the columns we need and rename them so they are easier to read
    # We check if 'classif1.label' (Age Group) exists because Informal Employment might not have it
    if 'classif1.label' in df.columns:
        df = df[['ref_area.label', 'indicator.label', 'sex.label', 'classif1.label', 'time', 'obs_value', 'obs_status.label']]
        df.columns = ['Country', 'Indicator', 'Sex', 'Age_Group', 'Year', 'Value', 'Observation_Status']
    else:
        df = df[['ref_area.label', 'indicator.label', 'sex.label', 'time', 'obs_value', 'obs_status.label']]
        df.columns = ['Country', 'Indicator', 'Sex', 'Year', 'Value', 'Observation_Status']
    
    # Add this cleaned table to our main list
    all_cleaned_data.append(df)
    
    # Count how many countries are left in this file and print it
    country_count = df['Country'].nunique()
    print("Found", country_count, "Sub-Saharan African countries in this file.")
    print("---")

# 5. Combine all the cleaned tables into one big table
final_dataset = pd.concat(all_cleaned_data, ignore_index=True)

# 6. Fill in missing observation status values with the word 'Observed'
final_dataset['Observation_Status'] = final_dataset['Observation_Status'].fillna('Observed')

# 7. Create the output folder (data/processed) if it does not already exist
save_folder = os.path.join(folder_path, "data", "processed")
os.makedirs(save_folder, exist_ok=True)

# 8. Save the combined data as a CSV file
save_path = os.path.join(save_folder, "curated_dataset.csv")
final_dataset.to_csv(save_path, index=False)

print("All done! The combined dataset has", len(final_dataset), "rows.")
print("It is saved at:", save_path)
