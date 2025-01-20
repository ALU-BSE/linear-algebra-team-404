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

# Iterate over each row in the Prices matrix
for i in range(len(Prices)):
    # Initialize the sum for the current row
    row_sum = 0
    # Iterate over each column in the current row
    for j in range(len(Prices[0])):
         # Multiplying the current element in the row with the corresponding element in Array2 and add to the row sum
         row_sum += Prices[i][j] * Array2[j]
    # Append the row sum (dot product) to the Ans list
    Ans.append(row_sum)


print(Ans)

# Participants
#Akoto-Nimoh Christine Serwaa
#John Ongeri Ouma

#github repo : https://github.com/ALU-BSE/linear-algebra-team-404.git