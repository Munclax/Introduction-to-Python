x=100 
def local_var():
  global x #doesn't create a local x and rather works on the global variable created previously
  x=11
  print("Local Variable value:",x)
local_var()
print("Global Variable value:",x)
#as seen both the local and global variable are now same as it was modified within the function through global keyword