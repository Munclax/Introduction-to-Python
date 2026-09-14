#enumerate() function is used to iterate over a list and get the index and value of each item in the list. It returns a tuple containing the index and value of each item in the list.
names=["a","b","c","d"]
name='Prem'
for i in enumerate(names): #returns a tuple containing the index and value of each item in the list.
  print(i)
for j in enumerate(name): #returns a tuple containing the index and value of each character in the string.
  print(j)