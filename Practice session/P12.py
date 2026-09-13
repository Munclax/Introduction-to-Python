#use of continue statement in for loop to print even numbers from 1 to 20
for i in range(1,20):
 if i%2!=0:
    continue
 print(i)

#without using continue statement
#for i in range(1,20):
#  if(i%2==0):
#    print(i)