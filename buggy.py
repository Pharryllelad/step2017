'''
	This program is full of different types of
	bugs that causes the program to crash,  
	not run, and generally not behave properly

'''

# Part 1
# Lets start off simple

name = input("What is your name:")
print('hello', name)
print('\n\n\n')
# Part 2
# Nice lets try to knock it up a knotch
# Triangles are strong shapes, I wonder what the hypotenous is

import math 

a = 3
b = 4

c = math.pow(a, 2) + math.pow(b, 3)
c = math.sqrt(c)
print('the hypotenous is', c)
print('\n\n\n')
# Continue once it prints out 5

# Part 3
# Good work, this next one is a little more complex
# its based on loops
# hint: make sure your code doesnt run in circles forever

i = 2
total = 0
while(i != 10):
	total = total + i
	i += 2


print('the total is', total)
print('\n\n\n')
# Continue if it prints out sum of odd numbers from 1 - 9 (25)

# Part 4
# Last one here is a challenge
# Time to make decisions

age = input('Enter your age => ') # Hint, your age is a number

if age < 10:
	print('almost double digits')

elif age < 50:
	print('almost half way to a 100')

if age > 50:
	print('hmm, this feels like its repeating)

elif age < 50:
	print("wow, older than 50)"

# once you get it running, are all cases handled, is there an age
# that you forgot to consider'
