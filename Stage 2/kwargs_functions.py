#**kwargs function somewhat like the *args as in it creates as many parameters as recquired for defining the function but rather than creating a tuple like *args it creates a dictionary as show in the example below
def student(**details):
  print(details["name"])
  print(details["year"])
  print(details["course"])
student(name="Premanshu",year=4,course="CSE")
#Note: student() is the function we created while details is the dictionary created and can access the values through it