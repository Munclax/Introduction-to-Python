#split() function is used to split a string into a list where each word is a list item. By default, it splits the string at whitespace.
s=input("Enter the subjects:")
subjects=s.split() #this will split the input string into a list of subjects
print(subjects) #prints the entire list of subjects
print(subjects[0])
print(subjects[-1])