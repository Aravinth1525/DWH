import numpy as np
from apyori import apriori
import pandas as pd

itemset = pd.read_csv("/Users/aravinth/Desktop/Data Warehousing/Data.csv")
print(" ")
print(itemset)
print(" ")

a=itemset.shape
print(a)

l1=[]
for i in range (0,6):
    l1.append([str(itemset.values[i,j]) for j in range (0,5)])

print(" ")
print(l1)
print(" ")

assosiation_rules=apriori(l1,min_support=0.5,min_confidence=1,min_length=2)
result=list(assosiation_rules)
print("Length is",len(result))
print(" ")
print(result)
print(" ")

