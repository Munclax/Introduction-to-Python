#continue keyword is used to skip the current iteration of the loop and move to the next iteration. It can be used in both for and while loops.
for i in range(1,10):
    if i%2==0:
        continue #if the number is even, it will skip the current iteration and move to the next iteration.
    print(i) #it will print the odd numbers from 1 to 9.