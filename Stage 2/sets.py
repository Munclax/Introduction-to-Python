#sets are unordered collections of unique elements. They are defined using curly braces {} or the set() constructor. Sets
sets={1,2,2,3,4,5,6,7,8}
print(sets)
print(type(sets))
sets.add(9) #add() method adds an element to the set. If the element already exists, it will not be added again.
print(sets)
sets.remove(2) #remove() method removes an element from the set. If the element does not exist, it will raise a KeyError.
print(sets)
sets.clear() #clear() method removes all elements from the set.
print(sets)