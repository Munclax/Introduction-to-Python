#A program to 
students = { "Prem": {"age": 21, "course": "CSE", "marks": 99},"Rahul": {"age": 20, "course": "ECE", "marks": 86},"Ayan": {"age": 21, "course": "CSE", "marks": 92}}
print("\t\t\tStudent Management system")
print("\n1. View all students\n2. Search for a student\n3. Add a student\n4. Update marks\n5. Delete a student\n6. Show statistics\n7. Exit")
in1=int(input("Please enter your choice:"))
while in1!=7:
  if in1==1:
    print("The students currently present in the database are:")
    for student, details in students.items():
      print(student)
    in1=int(input("Enter you next choice of operation:"))
  elif in1==2:
    in2=input("Please enter a name to search in the database:")
    check=False
    for student, details in students.items():
      if in2==student:
        check=True
    if check:
      print(in2,"is present in our database.")
    else:
      print(in2,"is NOT present in our database.")
    in1=int(input("Enter you next choice of operation:"))
  elif in1==3:
    print("You have selected the option to add to the database.......")
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    marks = int(input("Enter marks: "))
    details={"age": age, "course": course, "marks": marks}
    students.update({name:details})
    in1=int(input("Enter you next choice of operation:"))
  elif in1==4:
    print("You have selected the option to edit marks of a student from the database.......")
    name2=input("Enter the name of the student:")
    check2=False
    for student,details in students.items():
      if name2==student:
        marks2=int(input("Enter marks: "))
        details["marks"]=marks2
        check2=True
    if check2==False:
      print("Please check the name of student and verify it exists in the database......")
    in1=int(input("Enter you next choice of operation:"))
  elif in1==5:
    print("You have selected the option to delete the data of a student from the database.......")
    name3 = input("Enter student name: ")
    if name3 in students:
      del students[name3]
    else:
      print("Please check the name of student and verify it exists in the database......")
    print("The remaining student names in the databse are:")
    for student, details in students.items():
      print(student)
    in1=int(input("Enter you next choice of operation:"))
  elif in1==6:
    avg=0
    count=0
    total=0
    high=None 
    high_stu="" 
    low=None 
    low_stu=""
    for student,details in students.items():
      marks=details["marks"]
      if high is None or marks>high:
        high=marks
        high_stu=student
      if low is None or marks<low:
        low=marks
        low_stu=student
      total+=marks
      count+=1
    if count>0:
       avg=total/count
    print("Average marks of students:",avg)
    print("Highest marks:",high,"by student:",high_stu)
    print("Lowest marks:",low,"by student:",low_stu)
    in1=int(input("Enter you next choice of operation:"))
if in1==7:
    print("You have selected the option to exit the program.......")
    exit()