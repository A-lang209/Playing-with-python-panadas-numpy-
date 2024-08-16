import pandas  as pd
import numpy as np

s1 = pd.Series([1,2,3,4,5,])
s1

pd.Series(['red', 'blue', 'green'])

n1 = np.array([[1,2,3], [4,5,6], [7,8,9]])
df1= pd.DataFrame(n1)
df1

l2 = [1,2,3,4,5]
s2 = pd.Series(l2, name='A')
s2

l2 = [1,2,3,4,5]
s2 = pd.Series(l2)
s2

#Creating a DataFrame from a Numpy array
n2 = np.array([[1,2,3], [4,5,6], [7,8,9]])
#Creating columns name
#df2 = pd.DataFrame(n2, columns=['A', 'B', 'C'])
#df2
#Creating columns and rows name
df3 = pd.DataFrame(n2, columns=['A', 'B', 'C'], index=['R1', 'R2', 'R3'])
df3

#To have an index with new names we have to create a new DataFrame
df4 = df3.copy()
df4.index = ['John', 'Bodz', 'Jane']
df4

#Creating a DataFrame from a dictionary
d = {'A': [1,2,3], 'B': [4,5,6], 'C': [7,8,9]}
df1.index = ['John', 'Bodz', "Sally"]
df1
