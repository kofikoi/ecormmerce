import pandas as pd

# Read the CSV file into a pandas dataframe
df = pd.read_csv('vehicles.csv')

# Convert the dataframe to a JSON object
data = df.to_json(orient='records')

# Write the JSON object to a file
with open('vehicles.json', 'w') as f:
    f.write(data)
