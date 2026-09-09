print("Welcome to the guessing game!")
guest_input=int(input("Enter your guess"))
num=8
while (guest_input!=8):
  if(guest_input<8):
    print("Too low")
  if(guest_input>8):
    print("Too high")
  guest_input=int(input("Enter another guess"))
if(guest_input==num):
  print("You guessed correct!")