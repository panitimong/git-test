import pandas as pd
import numpy as np

# 1. Create your dictionary of lists
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}

# 2. Pass it directly to the DataFrame constructor
df = pd.DataFrame(data)

# Create a new column based on age
df['Age_Group'] = np.where(df['Age'] >= 30, 'Senior', 'Junior')
print(df)