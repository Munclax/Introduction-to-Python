#write a python program to print the following pattern
#*****
#****
#***    
#**
#*
for i in range(5,0,-1):
  for j in range(i):
    print("*",end=" ")
  print()