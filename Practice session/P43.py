#a program to print the highest,lowest,total and average from the number of marks entered by the user.
def student(*marks):
  high=None
  low=None
  total=0
  count=0
  for mark in marks:
    if high is None or mark>=high:
      high=mark
    if low is None or mark<=low:
      low=mark
    total=total+mark
    count+=1
  return count,total,high,low
p=int(input("Enter Physics marks:"))
c=int(input("Enter Chemistry marks:"))
m=int(input("Enter Maths marks:"))
c,t,h,l=student(p,c,m)
avg=t/c
print("Total obtained:",t,"out of:",(c*100))
print("Average:",avg)
print("Highest marks:",h)
print("Lowest marks:",l)