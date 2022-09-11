import pandas as pd
import numpy as np

list=[10,20,30,40,50,60,70,80,90,100]
ser=pd.Series(list)
a=[1,3]
b=ser.loc[a]
print(b)
c=ser.take(a)
print(c)