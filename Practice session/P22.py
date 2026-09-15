#write a python program to print the following pattern
#*
#**
#***
#****
#*****
for i in range(1,6):
  for j in range(i):
    print("*",end=" ")
  print()