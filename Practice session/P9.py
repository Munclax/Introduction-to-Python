#modify the guessing game program to count the number of guesses the user made before guessing the correct number
print("Welcome to the guessing game!")
guest_input=int(input("Enter your guess"))
num=8
count=0
while (guest_input!=8):
  if(guest_input<8):
    print("Too low")
  if(guest_input>8):
    print("Too high")
  guest_input=int(input("Enter another guess"))
  count+=1
if(guest_input==num):
  print("You guessed correct!")
  print("You need a total of",count,"guesses. Thanks for playing.")