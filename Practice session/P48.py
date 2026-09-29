count=0
def increase():
  global count #this uses the global count variable instead of creating a local variable inside the function
  count+=1
increase() #calls the function for the first time making the count increment to 1
increase()
increase()
print("Value of count after 3 calls:",count) #count now prints 3 being called 3 times incrementing the value 1 at a time