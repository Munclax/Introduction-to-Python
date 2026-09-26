#a program to accept lists of marks and then print out the total,highest,lowest and an average.
def mark(*m):
  high=low=m[0]
  total=0
  count=0
  for i in m:
    if i>=high:
      high=i
    elif i<=low:
      low=i
    count+=1
    total=total+i
  return total,high,low,count
t,h,l,c=mark(21,21,34,42,15,43,89)
avg=t/c
print("Total marks:",t,"\nHighest marks:",h,"\nLowest marks",l,"\nAverage marks:",avg)