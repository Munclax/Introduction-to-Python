#write a program to print the names of your family members in reverse order using while loop and len() function.
#Sol:
name=["Prem","Mistu","Mum","Baba"]
length=len(name)
index=length-1
while index>=0:
  print(name[index])
  index-=1