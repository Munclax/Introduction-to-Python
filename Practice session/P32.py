#write a python program to check whether a student is a student of MIT or not.
name={"Prem","Ananda","Piru","Shubham","Saikat","Gopi"}
n=input("Enter the name of student:")
bool=False
for i in name:
  if n==i:
    bool=True
if bool==True:
  print(n,"is a student of MIT.")
else:
  print(n,"isn't a student of MIT.")