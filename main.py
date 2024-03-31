import pandas as pd

# Specify the file path
file_path = 'All_GPUs.csv'

# Load the CSV file into a pandas DataFrame
data = pd.read_csv(file_path)

# Print the loaded data
#print(data)

data.dropna(inplace=True)
print(data)


# multiple linear regression



