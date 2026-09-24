def cal(a,b): 
  return a+b,a*b,a-b #return can well return multiple values as a list from a function
#print(cal(1,2)) You can run this to check the working
a=int(input("Enter your first number:"))
b=int(input("Enter your second number:"))
add,multiply,subtract=cal(a,b)
print("Sum:",add)
print("Product:",multiply)
print("Difference:",subtract)
