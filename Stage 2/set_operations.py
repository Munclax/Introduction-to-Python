a={1,2,2,3,4,5,6,7,8}
b={7,8,9,10,11}
print(a.intersection(b)) #intersection() method returns a new set with elements that are common to both sets.
print(a&b) #'&' operator returns a new set with elements that are common to both sets.
print(a.union(b)) #union() method returns a new set with elements from both sets.
print(a|b) #'|' operator returns a new set with elements from both sets.
#c=a.intersection(b) also works but it is not recommended to use it because it creates a new set and assigns it to c. It is better to use the '&' operator because it does not create a new set and is more efficient.
print(a.difference(b)) #difference() method returns a new set with elements that are in the first set but not in the second set.
print(a-b) #'-' operator returns a new set with elements that are in the first