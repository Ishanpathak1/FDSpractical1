import pandas as pd
import numpy as np

arr=np.array(['Ishan','Vedant','Dhara','Vishal','Jay'])
ser1=pd.Series(arr)
print(ser1)
print("\n")

dict1={'Name':'Ishan Pathak', 'Age':21, 'Degree':'B.tech', 'Semester':5}
ser2=pd.Series(dict1)
print(ser2)
print("\n")

list1=[10,20,30,40,50]
alpha=pd.Series(list1)
print(alpha)
print("\n")

list2=[60,70,80,90,100]
beta=pd.Series(list2)
print(beta)
print("\n")

pd.DataFrame(alpha,beta)
pd.concat([alpha,beta])

details= {
    'Name' :['Ishan','Vedant','Dhara','Jay'],
    'Age' :[20,21,22,21],
    'University' : ['ITMBU','ITMBU','ITMBU','ITMBU']
}
df=pd.DataFrame(details)
print(df)