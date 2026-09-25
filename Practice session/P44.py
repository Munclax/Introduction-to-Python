#write a program to take as many numbers as possible from user and return their sum using functions.
def sum(*num):
  s=0
  for n in num:
    s=s+n
  return s
numbers=input("Enter your numbers:")
string_list=numbers.split()
num_list=[int(n) for n in string_list]
print("The total sum is:",sum(*num_list))