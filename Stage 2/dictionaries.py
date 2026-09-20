#dictionaries are unordered collections of key-value pairs. They are defined using curly braces {} or the dict() constructor. Dictionaries are mutable, meaning that their elements can be changed, added, or removed. Keys in a dictionary must be unique and immutable (e.g., strings, numbers, tuples), while values can be of any data type and can be duplicated.
#{key: value} is the syntax for defining a dictionary. Keys are used to access the corresponding values in the dictionary.
info={"name":"Premanshu","age":21,"language":"English","team":"Manchester United"}
print(info["name"]) #prints the value associated with the key "name"
info["country"]="India" #adds a new key-value pair to the dictionary. If the key already exists, its value will be updated.
print(info) 
info["language"]="Hindi" #updates the value associated with the key "language". If the key does not exist, a new key-value pair will be added to the dictionary.
del(info["name"]) #removes the key-value pair associated with the key "name" from the dictionary. If the key does not exist, a KeyError will be raised.
print(info) 
print(info.clear()) #removes all key-value pairs from the dictionary, leaving it empty. The clear() method does not return any value, so it will print None.