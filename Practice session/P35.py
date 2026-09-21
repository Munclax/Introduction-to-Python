#write a program to check if a fruit is present in the inventory or not.
inventory={"Apple":20,"Banana":42,"Orange":12,"Kiwi":5,"Strawberry":10}
user=input("Enter the fruit to check for:")
check=False
for i,j in inventory.items():
  if user==i:
    check=True
if check==True:
  print(user,"is present in the inventory.")
else:
  print(user,"is not present in the inventory.")
  
