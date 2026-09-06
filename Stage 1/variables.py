name="Premanshu" #this variable stores a string value
age=21 #this variable stores an integer value
stream="Computer Science" #this variable stores a string value
print(name,age,stream) # ',' concatenates the values of the variables
print(age+2) #'+' mathematically adds the value of integer variales
print(name + stream) # '+' here  concatenates the string variables
#print(name + age) this doesn't work because we can't concatenate a string and an integer
print("My name is", name, "and I am", age, "years old. I am pursuing", stream)
print(type(name)) # type() prints the data type of a variable
print("Variable type of age", type(age))
age_str=str(age) # this converts the integer variable 'age' into a string variable; this is known as type casting
print("Variable type of age after type casting", type(age_str)) 
result= age>=18 # this variable stores a boolean value; it returns true if the condition is met, otherwise it returns false
print("Is age greater than or equal to 18?", result)
print(type(result)) # type() prints the data type of a variable