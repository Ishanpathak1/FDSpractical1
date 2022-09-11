import pandas as pd
list1=[10,20,30,40,50]
alpha=pd.Series(list1)
print(alpha)
print("\n")

list2=[50,70,80,90,100]
beta=pd.Series(list2)
print(beta)
print("\n")

print("Items not common in Series alpha and beta are")
a=alpha[~alpha.isin(beta)]
b=beta[~beta.isin(alpha)]
c=pd.concat([a,b])
print(c)
