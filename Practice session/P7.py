#write a program to count the number of times 2 appeared in a list of numbers
numbers=[2,3,45,2,35,20,2]
length=len(numbers)
count=0
index=0
while index<length:
  if(numbers[index]==2):
    count+=1
  index+=1
print("Total number of times 2 appeared in the list:",count)