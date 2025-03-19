import pandas as pd
import openpyxl

# The following are the validation checks for the data to be applied

'''
Null or Missing Values | Duplicates | Outliers
Data Type Validation | Range Checks | Consistency Checks
Unique Value Checks | Business Rule Validations
'''
# load the given excel file and read
file_path = '/Users/krishnatagirisa/my_env/LLM/Before_QC.xlsx'
data = pd.read_excel(file_path)

# Display first few rows
print('first few rows: \n', data.head())

# Display last few rows
print('last few rows: \n', data.tail())

# remove empty cells - One way to deal with empty cells is to remove rows 
# that contain empty cells.
new_df = data.dropna()

print('after removal of empty cells/rows: \n',new_df.to_string())

