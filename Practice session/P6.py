#write a program to find the biggest number in a list of numbers.
#Solution:
numbers=[12,34,56,6,21,80,21]
length=len(numbers)
count=0
biggest=numbers[0]  # Initialize biggest with the first element
while count<length:
  if numbers[count]>=biggest:
    biggest=numbers[count]
  count+=1
print("The biggest number is:", biggest)