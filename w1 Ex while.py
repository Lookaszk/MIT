Exercise: while exercise 1
5/5 points (graded)
ESTIMATED TIME TO COMPLETE: 5 minutes

In this problem you'll be given a chance to practice writing some while loops.

1. Convert the following into code that uses a while loop.

print 2
prints 4
prints 6
prints 8
prints 10
prints Goodbye!

Code Editor

1
num = 2
2
while num < 12:
3
    print (num)
4
    num += 2
5
print ("Goodbye!")
Press ESC then TAB or click outside of the code editor to exit
correctCorrect
Test results
CORRECT See full outputSee full output
Submit Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

Show Answer
Correct (5/5 points) Review
Exercise: while exercise 2
5/5 points (graded)
ESTIMATED TIME TO COMPLETE: 5 minutes

2. Convert the following into code that uses a while loop.

prints Hello!
prints 10
prints 8
prints 6
prints 4
prints 2

Code Editor

1
total = 10
2
step = -2
3
print("Hello!")
4
while total > 0:
5
    print(total)
6
    total += step
Press ESC then TAB or click outside of the code editor to exit
correctCorrect
Test results
CORRECT Hide outputHide output
What's printed?
Output:
Hello!
10
8
6
4
2

Submit Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

Show Answer
Correct (5/5 points) Review
Exercise: while exercise 3
5/5 points (graded)
ESTIMATED TIME TO COMPLETE: 5 minutes

3. Write a while loop that sums the values 1 through end, inclusive. end is a variable that we define for you. So, for example, if we define end to be 6, your code should print out the result:

21
which is 1 + 2 + 3 + 4 + 5 + 6.

For problems such as these, do not include input statements or define variables we will provide for you. Our automating testing will provide values so write your code in the following box assuming these variables are already defined.

Hint: Don't Use A Variable Called 'sum'
Code Editor

total = 0
i = 0
while i <= end:
    total += i
    i += 1

print(total)
1
total = 0
2
i = 0
3
while i <= end:
4
    total += i
5
    i += 1
6
 
7
print(total)
