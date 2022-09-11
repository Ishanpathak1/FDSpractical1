import pandas as pd
ser1=pd.Series([10,10,20,30,10,30,20,40,10,40,20,10,10])
a=ser1.value_counts()
print(a)