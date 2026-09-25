#a program to find the number of postive and negative numbers including zero from the user input.
def num(*inp):
  pos_count=neg_count=count=0
  for n in inp:
    if n>0:
      pos_count+=1
    elif n<=0:
      neg_count+=1
    else:
      count+=1
  return pos_count,neg_count,count
usr=input("Enter your numbers:")
str_list=usr.split()
num_list=[int(n) for n in str_list]
p,n,c=num(*num_list)
print("Number of positive numbers:",p,"\nNumber of negative numbers:",n,"\nNumber of zeros:",c)