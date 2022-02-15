"""
Given n as input. Print following pattern using For loop.
Input-> n = 4
Output-> 
1 
12 
123 
1234 
4 
43 
432 
4321
"""

n = 4
st_1 = ""
st_2 = ""
for i in range(1,n+1):
  st_1 = st_1 + str(i)
  print(st_1)
for j in range(n,0,-1):
  st_2 = st_2 + str(j)
  print(st_2) 
