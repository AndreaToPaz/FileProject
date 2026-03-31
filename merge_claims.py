import pandas as pd
import os

# Folder where your 98 files are located
folder_path = r"C:\Users\icarl\OneDrive\Escritorio\ClaimsFiles"

# Create empty list to store dataframes
all_data = []

# Loop through every file in folder
for file in os.listdir(folder_path):
    if file.endswith(".xlsx"):
        file_path = os.path.join(folder_path, file)
        
        # Read Excel file
        df = pd.read_excel(file_path)
        
        # Append dataframe to list
        all_data.append(df)

# Merge all dataframes
merged_df = pd.concat(all_data, ignore_index=True)

# Export merged file
output_path = r"C:\Users\icarl\OneDrive\Escritorio\Merged_Claims.xlsx"
merged_df.to_excel(output_path, index=False)

print("✅ All files merged successfully!")