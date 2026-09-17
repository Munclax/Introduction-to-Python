#write a python program to accept the name of students and subjects and display the name of students with the subjects they study.
s=input("Enter the subjects:")
subjects=s.split()
stu=input("Enter the name of students:")
student=stu.split()
for stud in student:
  print(stud,"studies the following subjects:")
  for sub in subjects:
    print(sub)
  print()