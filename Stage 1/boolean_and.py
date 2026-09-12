age=int(input("Enter your age: "))
has_id=input("Do you have an ID? (True/False): ")
if(age>=18 and (has_id==True or has_id=="true")): #and returns true if both the conditions are true, otherwise it returns false
    print("You are eligible to vote.") #if both conditions are met, then the person is eligible to vote
else:
    print("You are not eligible to vote.")