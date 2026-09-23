#write a function to get the average of numbers input by the user.
def avg(a,b,c):
  return (a+b+c)/3
i=int(input("Enter your values:"))
j=int(input("Enter your values:"))
k=int(input("Enter your values:"))
result=avg(i,j,k)
print("The average of the numbers:",result)