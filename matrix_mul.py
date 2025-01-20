import pandas as pd
import numpy as np

# Load data
# created a sample data to test pandas
data  = pd.read_csv('Data.csv')

# Example arrays
Prices = [[300, 500],
          [1000, 120.85]]

Array2 = [200, 100]

# Calculate the result
Ans = []
# (300*200 + 500*100) as an example calculation

for i in range(len(Prices)):
    row_sum = 0
    for j in range(len(Prices[0])):
         row_sum += Prices[i][j] * Array2[j]
         Ans.append(row_sum)
        #pass


print(Ans)
