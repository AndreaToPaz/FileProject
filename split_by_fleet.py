import pandas as pd
import os
import re

# Path to master file
master_file = r"C:\Users\icarl\OneDrive\Escritorio\Claim copuy.xlsx"

# Define ONE output folder called "Fleet_Files"
output_folder = r"C:\Users\icarl\OneDrive\Escritorio\Fleet_Files"

os.makedirs(output_folder, exist_ok=True)

# Read master file
df = pd.read_excel(master_file)

# -------------------------
# Clean column names robustly
# -------------------------
def clean_column(col):
    if isinstance(col, str):
        # Remove leading/trailing spaces
        col = col.strip()
        # Replace non-breaking spaces and other whitespace characters
        col = re.sub(r'\s+', ' ', col)
    return col

df.columns = [clean_column(c) for c in df.columns]

# Debug: print all column names to confirm
print("Columns after cleaning:", df.columns.tolist())

# -------------------------
# Check if the target column exists
# -------------------------
target_column = "Last delivery fleet"
if target_column not in df.columns:
    raise KeyError(f"Column '{target_column}' not found. Available columns: {df.columns.tolist()}")

# -------------------------
# Split by fleet and save
# -------------------------
for fleet_name, fleet_data in df.groupby(target_column):
    # Make fleet name safe for file naming
    safe_fleet_name = str(fleet_name).replace("/", "-").replace("\\", "-").replace(":", "-")
    
    
    # Create output path
    output_path = os.path.join(output_folder, f"{safe_fleet_name}.xlsx")
    
    # Save to Excel
    fleet_data.to_excel(output_path, index=False)

print("✅ All fleet files saved inside 'Fleet_Files' folder.")