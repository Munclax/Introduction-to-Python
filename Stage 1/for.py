#write a program using for loop to check if a name is present in the list or not.
#for loop is used to iterate over the list and perform operations on each element of the list. In this case, we are checking if the input name is present in the list of names.
names=["A","B","C","D"]
search=input("Enter your name:")
found=False
for name in names: #for loop is used to iterate over the list of names
  if search == name:
    found=True
    break
if found==True:
  print("Your name is present on the list.")
else:
    print("Your name is NOT present on the list.")
    