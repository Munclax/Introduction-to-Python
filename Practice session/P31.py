#write a python program to count the number of even numbers in a set of integers. Ignore duplicates.
sets={12,23,12,30,45,32,16,80,21,34,62} #set initialization
count=0
print("The even numbers in the set are:")
for s in sets:
  if s%2==0:
    print(s)
    count+=1
print("The total number of even numbers(ignoring duplicates):",count)