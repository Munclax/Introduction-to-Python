def student(**details):
  for info,detail in details.items():
    print(info,":",detail)
student(name="Premanshu",year=4,course="CSE")
#we could use for statement to access the dictionary like we did previously even do its inside a function