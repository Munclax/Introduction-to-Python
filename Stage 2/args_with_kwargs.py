def student(*subjects,**details):
  print("Subjects:")
  for i in subjects:
    print(i)
  print("\nStudent Details:")
  for info,detail in details.items():
    print(info,":",detail)
student("Physics","Maths","Chemistry",name="Premanshu",year=4,course="CSE")
# *args and **kwargs can be combined together inside functions to be used together.