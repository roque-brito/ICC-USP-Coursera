import pandas as pd 
s = pd.Series([5, 2, 15, 13, 7, 10])
print(s[s.between(0, 20)])
