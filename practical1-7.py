import pandas as pd
import numpy as np
list1=[10,20,30,40,50,60,70,80,90,100]
ser1=pd.Series(list1)
print("The Original Series is:")
print(ser1)
answer=np.where(ser1%3==0)
print("Positions of numbers who are multiple of 3 are: ")
print(answer)