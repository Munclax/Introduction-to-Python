#local variables are accessible within a function while a global variable can be accessed across the entire code
x=100 #this variable is defined as a global variable
def local_var():
  x=11 #this variable is defined as a local variable defined inside a function
  print("Local Variable value:",x)
local_var()
print("Global Variable value:",x)