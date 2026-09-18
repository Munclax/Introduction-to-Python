#slicing refers to obtaining a portion of a list by specifying a start index, stop index, and an optional step value. The syntax for slicing is list[start:stop:step].
numbers=[10,20,30,40,50,60,70,80,90]
print(numbers) #prints the entire list
print(numbers[1:4]) #list[start:stop] prints elements from index 1 to index 3
print(numbers[:4]) #list[:stop] prints elements from the beginning of the list to index 3
print(numbers[1:]) #list[start:] prints elements from index 1 to the end of the list
print(numbers[1:7:2]) #list[start:stop:step] prints elements from index 1 to index 6 with a step of 2
print(numbers[::-1]) #list[::-1] prints the entire list in reverse order