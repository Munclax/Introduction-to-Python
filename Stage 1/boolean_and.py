age=int(input("Enter your age: "))
has_id=input("Do you have an ID? (True/False): ")
if(age>=18 and (has_id==True or has_id=="true")):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")