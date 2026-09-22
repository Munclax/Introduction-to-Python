
students = {"Prem": {"age": 21,"course": "CSE","marks":99}, "Rahul": {"age": 20,"course": "ECE","marks": 78}, "Ayan": {"age": 21,"course": "CSE","marks": 92}} 
students.update({"Rahul": {"age": 20,"course": "ECE","marks": 86}})
students.update({"Priya": {"age": 22,"course": "CSE","marks": 82}})
user=input("Enter student name:")
check=False
avg=0
count=0
total=0
high=None 
high_stu="" 
low=None 
low_stu=""
for student,details in students.items():
    if user==student:
     check=True
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
if check==True:
  print(user,"'s marksheet info does exist in the database.'")
else:
   print(user,"'s marksheet info doesNOT exist in the database.'")
print("Average marks of students:",avg)
print("Highest marks:",high,"by student:",high_stu)
print("Lowest marks:",low,"by student:",low_stu)