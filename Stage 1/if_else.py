name=input("Please enter your name: ") # this will take input from the user
age=int(input("Please enter your age: ")) # this will take input from the user, convert it to an integer 
if(age>=18): #if statement returns true if the condition is met, otherwise it returns false
    print(name,",you are eligible to vote.")
else: #else statement executes if the condition in the if statement is not met
    print("You are not eligible to vote.")