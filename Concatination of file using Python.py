

# Importing important liabraries
import pandas as pd 
import os

# path of files
path = r"d:\rg67266\Downloads\SalesData"

# read the 1 month datasets
df1 = pd.read_csv(fr"{path}\Sales_April_2019.csv")

# take all files from the path
files = os.listdir(path)

# create the empty dataframe
df = pd.DataFrame()

# Playing with loop
for file in files:
    mdf = pd.read_csv(f"{path}\{file}") # Read the data sets for 12 month
    df = pd.concat([df,mdf]) # Concate the all files in empty datasets

# read the all concat data sets for 12 months
print(df)

