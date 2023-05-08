import pandas as pd


# Load Excel file

df = pd.read_csv('data.csv', skiprows=1)

df_odd = df.iloc[::2]

# write the DataFrame to a new Excel file with a sheet named 'odd_rows'
df_odd.to_csv('realtors.csv', index=False)

