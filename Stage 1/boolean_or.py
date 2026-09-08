is_employee=input("Are you an employee? (Yes/No): ")
is_student=input("Are you a student? (Yes/No): ")
password=input("Enter your password: ")
if((is_employee=="yes"or is_employee=="Yes")or (is_student=="yes"or is_student=="Yes")): #or returns true if any one of the conditions is true, otherwise it returns false
    if(password=="student" or password=="employee"): #if any one of the conditions is met, then the person is asked for the password 
        print("You are eligible for a discount.") #if any one of the conditions is met, and the password is correct the discount is applied
    else:
        print("You are not eligible for a discount.")
else:
    print("You are not eligible for a discount.")