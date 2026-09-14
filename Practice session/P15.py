#write a python program to print all the numbers from 0 to 20 except 8 using break statement
for i in range(20):
  if i==0:
    continue
  if i==8:
    break
  print(i)