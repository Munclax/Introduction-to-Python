def calc_price(mrp,quantity):
  return mrp*quantity
m=int(input("Enter the MRP of the item:"))
q=int(input("Enter the quantity:"))
print("Your total bill:",calc_price(m,q))

