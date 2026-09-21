#this program calculates the total, average, highest and lowest marks obtained in different subjects using dictionary and loops
marks={"Maths":98,"Physics":82,"Chemistry":89,"Biology":93,"Computer":100}
total=0
highest=None
highest_sub=""
lowest=None
lowest_sub=""
count=0
print("The subjects are:")
for i,j in marks.items():
  print(i,end=" ")
  total=total+j
  if highest is None or j>highest:
    highest=j
    highest_sub=i
  if lowest is None or lowest>j:
    lowest=j
    lowest_sub=i
  count+=1
average=total/count
print("\nTotal number of subjects:",count)
print("Total marks obtainable:",count*100)
print("Total marks obtained:",total)
print("Total average marks:",average)
print("The highest marks obtained is:",highest,"at",highest_sub)
print("The lowest marks obtained is:",lowest,"at",lowest_sub)