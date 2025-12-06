import numpy as np
import re

# read file and close it
f = open("input.txt","r")
lines = f.readlines()
f.close()

# get all the operations that will be done
operations = lines[-1].replace(" ","")
# print(operations)

# count the number of rows for each operation
numbers_per_operation = len(lines)-1

# get the first row of numbers and split it with spaces
num_array = re.split(" ",lines[0].strip())

# cast strings to integers (if the output of the splitting is numering)
actual_numbers = np.array([int(num) for num in num_array if num.isnumeric()])

# get the number of numbers per row
nums_per_line = len(actual_numbers)

# create a numpy array with all the numbers of the file
numbers = np.zeros([numbers_per_operation,nums_per_line])

# populate the first row
numbers[0,:] =  actual_numbers

# do the same for all the rows in the text file
for i in range(1,numbers_per_operation):
    num_array = re.split(" ",lines[i].strip())
    numbers[i,:] = np.array([int(num) for num in num_array if num.isnumeric()])

# initialise grand total
grand_total = 0

# read every column of the "numbers" matrix and perform the appropriate operation
# and add it to the grand total
for j in range(nums_per_line):

    if operations[j] == "*":
        grand_total += int(np.prod(numbers[:,j]))
    else:
        grand_total += int(np.sum(numbers[:,j]))

# print result
print(grand_total)
