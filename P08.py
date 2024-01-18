# Write a Pandas program to convert the first column of a DataFrame as a Series.

import pandas as pd

# Create a DataFrame
data = {'A': [1, 5, 3, 8, 2],'B': [4, 7, 2, 9, 5]}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

df_as_list1 = df['A'].tolist()

print("Type :-",type(df_as_list1))
print(df_as_list1)