import pandas as pd
import glob

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    data = pd.read_excel(filepath, sheet_name="Sheet 1")
    print(data)
