#a calculator program to print highest, lowest, total , average and lastly the number of values.
def calculator(*m):
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
t,h,l,c=calculator(21,21,34,42,15,43,89)
avg=t/c
print("Total:",t,"\nHighest:",h,"\nLowest",l,"\nAverage:",avg,"\nNumber of values:",c)