f = open("input.txt","r")

joltage_nums = []

for line in f: # for every bank of batteries
    volts = line.strip() # strip the input
    nums = [int(elem) for elem in volts] # cast to integers

    first_num = max(nums[:-1]) # # get the highest element of the array
    # we cannot consider the last element of the array  
    # because we wouldn't be able to create a 2-digit number otherwise

    # print(first_num)

    # get the index of the first occurence of this number we just found
    max_num_index = nums.index(first_num)

    # find the largest number after the one we just found
    second_num = max(nums[max_num_index+1:])
    
    # concatenate them and save them
    joltage_nums.append(int(str(first_num)+str(second_num)))

# Print everything and sum
print(joltage_nums)
print(sum(joltage_nums))

# close the document
f.close()