#This program is used to find the total number of fruits in the inventory and also to find the fruit taking the most and least inventory space.
inventory={"Apple":20,"Banana":42,"Orange":12,"Kiwi":5,"Strawberry":10}
print("The types of fruits available in the inventory:")
high=None
high_fru=""
low=None
low_fru=""
total=0
for fruit,number in inventory.items():
  print(fruit,end=" ")
  if high is None or number>high:
    high=number
    high_fru=fruit
  if low is None or number<low:
    low=number
    low_fru=fruit
  total=total+number
print("\nQuantities:",inventory.values())
print("\nThe total number of fruits in the inventory is:",total)
print("The fruit taking the most inventory space is:",high_fru,"taking a total space of:",high)
print("The fruit taking the least inventory space is:",low_fru,"taking a total space of:",low)