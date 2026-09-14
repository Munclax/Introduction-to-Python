#write a program to find the largest and smallest number in a list of numbers, count the number of even and odd numbers, and calculate the total sum of the numbers in the list.
numbers=[11,21,34,52,7,19,41]
largest=0
smallest=100
sum=0
even_count=0
odd_count=0
for num in numbers:
  if num>=largest:
    largest=num
  if num<=smallest:
    smallest=num
  if num%2!=0:
    odd_count+=1
  if num%2==0:
    even_count+=1
  sum=sum+num
print("The largest number is:",largest)
print("The smallest number is:",smallest)
print("The number of even numbers is:",even_count)
print("The number of odd numbers is:",odd_count)
print("The total sum is:",sum)