import pandas as pd
import numpy as np

nba_data = pd.read_csv('nbastats2018-2019.csv')
# print(nba_data)

# print(nba_data.columns)

# print(nba_data['FG3%'])

print(nba_data.sort_values('FG3%', ascending = False))

# for i in range(9):
#     print(nba_data['Name'][i])
#     print(nba_data['FG3%'][i])

# print(nba_data['Name'][0])