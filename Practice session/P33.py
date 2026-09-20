#This program counts the number of duplicate numbers in a given input. It prompts the user to enter a series of numbers, splits the input into individual numbers, and then uses a set to identify unique numbers. The difference between the total number of input numbers and the number of unique numbers gives the count of duplicates, which is then printed.
n=input("Enter the numbers:")
numbers=n.split()
s=set(numbers)
i=len(numbers)
j=len(s)
count=i-j
print("The total number of duplicates from the input:",count)
