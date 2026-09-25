#A program to figure out the average,total and highest marks scored by students using functions and return.
def result(a,b,c):
  high=0
  if a>=b and a>=c:
    high=a
  if b>=a and b>=c:
    high=b
  if c>=a and c>=b:
    high=c
  return a+b+c,(a+b+c)/3,high
p=int(input("Enter Physics Marks:"))
m=int(input("Enter Maths Marks:"))
c=int(input("Enter Chemistry Marks:"))
total,avg,h=result(p,m,c)
print("\nTotal:",total,"\nAverage:",avg,"\nHighest marks:",h)