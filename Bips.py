import pandas as pd
df = pd.read_csv('customer_shopping_behavior.csv')

# Wrap head() in a print function
print(df.head())

# This line is already correct and should be appearing
print(df.columns)
