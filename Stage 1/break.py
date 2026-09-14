#break keyword is used to break the loop when a certain condition is met. It can be used in both for and while loops.
numbers=[1,2,3,4,5,6,7,8,9]
length=len(numbers)
for num in numbers:
  if num==5: #if the number is equal to 5, the loop will break and exit the loop.
    break
  print(num) #it will print the numbers from 1 to 4 and then exit the loop when it reaches 5.