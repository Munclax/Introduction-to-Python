#write a python program to find the largest number in a list.
numbers=[20,30,12,35,76,54,81,11,92]
largest=0
for i in numbers:
  if largest<i:
    print("The current largest in the list is:",largest)
    largest=i
print("\n\nThe largest in the whole list is:",largest)