info={"Name":"Prem","Year":4,"Sem":7,"Department":"CSE"}
print(info.keys()) #keys() method returns a view object that displays a list of all the keys in the dictionary.
print(info.values()) #values() method returns a view object that displays a list of all the values in the dictionary.
print(info.items()) #items() method returns a view object that displays a list of tuples containing key-value pairs.
for key,value in info.items(): # Loop through each key-value pair in the dictionary.
  print(key,":",value)