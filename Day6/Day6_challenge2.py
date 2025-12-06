import math


# read file and close it
f = open("input.txt","r") 
lines = f.readlines()
f.close()

grand_total = 0 # initialise grand total

len_line = len(lines[0])-1 # count how many characters there are in each line without including "\n"
num_lines = len(lines) # count how many lines there are

i = len_line-1 # start from the last column of the text
curr_numbers = [] # keep track of what numbers need to be summed/multiplied

while i >= 0: # keep reading from the last to the first column of the text
    col = [lines[j][i] for j in range(num_lines)] # get the column
    
    curr_numbers.append(int("".join(col[:-1]))) # cast the numbers along each column to integers

    last_elem = col[-1] # get the last element of the column
    i-=1 # continue to next row

    
    if last_elem == " ": 
        #skip next steps if we do not need to perform the sum or multiplication
        continue 
    elif last_elem=="+": # if we need to perform a sum, add it to the grand total
        grand_total += sum(curr_numbers)
        # start collecting a new set of numbers
        curr_numbers = []
        # skip the following column because it will be all made up of spaces
        i-=1
    elif last_elem=="*": # if we need to perform a multiplacation, add it to the grand total
        grand_total += math.prod(curr_numbers)
        # start collecting a new set of numbers
        curr_numbers = []
        i-=1
        # skip the following column because it will be all made up of spaces

# print result
print(grand_total)