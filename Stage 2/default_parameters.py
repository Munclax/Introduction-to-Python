#a default parameter is used to assign values to the parameters of a fucntion as a default and can be later changed as needed within the code.
def student(name="A",course="XXX",year=00):
  return name,course,year
print(student())
n=input("Enter your name:")
c=input("Enter your Course:")
y=int(input("Enter your year of study:"))
print(student(n,c,y)) #the values of the default parameter are changed here