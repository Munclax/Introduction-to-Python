#Program to find average marks, highest and lowest marks of students using dictionary
students = {"Prem": {"age": 21,"course": "CSE","marks":99}, "Rahul": {"age": 20,"course": "ECE","marks": 78}, "Ayan": {"age": 21,"course": "CSE","marks": 92}} 
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