#while loop is used to execute a block of code repeatedly as long as a given condition is true. The condition is evaluated before executing the block of code. If the condition is true, the block of code is executed and the condition is evaluated again. This process continues until the condition becomes false.
print("Welcome to the guessing game!")
guest_input=int(input("Enter your guess:"))
num=8
while (guest_input!=8): #while loop is used to check if the guest_input is not equal to 8. 
  if(guest_input<8):
    print("Too low")
  if(guest_input>8):
    print("Too high")
  guest_input=int(input("Enter another guess"))
if(guest_input==num):
  print("You guessed correct!")