name=input("Enter your name: ")
marks=int(input("Enter your marks: "))
if (marks<50):
    print(name, "has scored an F grade")
elif (marks>=50 and marks<60):
    print(name, "has scored a D grade")
elif (marks>=60 and marks<70):
    print(name, "has scored a C grade")
elif (marks>=70 and marks<80):
    print(name, "has scored a B grade") 
elif (marks>=80 and marks<90):
    print(name, "has scored a A grade") 
elif (marks>90 and marks<=100):
    print(name, "has scored a S grade")
elif (marks>100):
    print(name, "Cmon dude, can we be serious?")      