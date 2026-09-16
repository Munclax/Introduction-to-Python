#range() function is used to generate a sequence of numbers. It can take one, two or three arguments. The first argument is the start value, the second argument is the stop value and the third argument is the step value. The start value is inclusive and the stop value is exclusive. The step value is optional and defaults to 1.
#range(stop) - it will generate numbers from 0 to stop-1
for i in range(10):
 print(i)
#range(start,stop) - it will generate numbers from start to stop-1
for i in range(2,10):
 print(i)
#range(start,stop,step) - it will generate numbers from start to stop-1 with a step of step
for i in range(2,10,3):
 print(i)