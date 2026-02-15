'''P-2.2Write a program to read text file data and create a dictionary of all keywords in the text file.
The program should count how many times each word is repeated.'''


words = 0
with open('sample.txt','r') as file:

	data = file.read()
	lines = data.split()
	words += len(lines)

# Printing total number of words
print(data)
print(lines)
print(words)
