#write a program to check if the user entered the correct password or not using while loop
#Solution:
password="Munchlax123"
usr_input=input("Enter your password:")
while usr_input!=password:
  print("Wrong Password. Please try again.")
  usr_input=input("Re-Enter your password please:")
if usr_input==password:
  print("Login success.")
  