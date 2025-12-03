f = open("input.txt","r")

joltage_nums = [] 

for line in f: # for every bank of batteries
    volts = line.strip() # strip the input
    nums = [int(elem) for elem in volts] # cast to integers

    l = len(nums) # get the amount of numbers we are dealing with
    # print(f"Length {l}")

    first_elem = max(nums[:l-11]) # get the highest element of the array
    # we cannot consider the last 11 elements of the array  
    # because we wouldn't be able to create a 12-digit number otherwise

    # get the index of the first occurence of this number we just found
    looking_after = nums.index(first_elem)

    # Keep track of everything
    indexes = [looking_after] # optional
    ordered_nums = [str(first_elem)]

    for i in range(1,12):
        # print(f"looking after index: {looking_after+1}")
        # print(f"Until {l-11+i}")
        # print(f"Looking at {nums[looking_after+1:l-11+i]}")

        elem = max(nums[looking_after+1:l-11+i]) # get maximum number in a
        # higher position from my previous element
        # (but still consider that we need to produce a 12-digit number)

        # get the first occurence of this number
        looking_after = nums[looking_after+1:l-11+i].index(elem) + looking_after +1

        # keep the number and cast it to a string (for concatenating purposes)
        ordered_nums.append(str(elem))
        # keep track of what where I found the joltage ratings I used
        indexes.append(looking_after)
    
    result = "".join(ordered_nums) # concatenate all the correct jolting ratings

    # print(result)
    # print(f"indexes {indexes}")

    joltage_nums.append(int(result)) # keep record of all the correct combinations

# Print everything and sum
print(joltage_nums)
print(sum(joltage_nums))

# close the document
f.close()