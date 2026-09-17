#write a python program to print all even numbers in a list
numbers=[20,30,12,35,76,54,81,11,92]
count=0
for i in numbers:
  if (i%2==0):
    print(i,",",end=" ")
    count+=1
print("\nThus the total number of even numbers is:",count)