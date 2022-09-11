import pandas as pd
list1=[10,20,30,40,50]
alpha=pd.Series(list1)
print(alpha)
print("\n")

list2=[50,70,80,90,100]
beta=pd.Series(list2)
print(beta)
print("\n")

print("Items in Series alpha only are")
common=alpha[~alpha.isin(beta)]
print(common)