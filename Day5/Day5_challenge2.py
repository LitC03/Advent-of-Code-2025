f = open("input.txt") # open the file and read it
lines = f.readlines()
f.close() # close it

separation = lines.index("\n") # get index of where the separation 
# happens between ranges and ingredients

# initialise arrays where the mins and maxs of the ranges will be collected
mins = [] 
maxs = []

# read ranges
i= 0
while i<separation: # stop reading lines if we encounter the empty line
    line = lines[i].strip()
    range_vals = line.split("-") # split the ranges into two

    # Cast to int and save ranges
    mins.append(int(range_vals[0])) # save the min values
    maxs.append(int(range_vals[1])) # save the max values of the ranges
    i+=1
    

# Sort the ranges accoring to their minimum values,
# for this reason the maximums need to be sorted with their corresponding minimum
ordered_maxs = [x for _, x in sorted(zip(mins, maxs))]
ordered_mins = sorted(mins)


# Attempt to merge all the ranges that overlap and obtained a
# collection of merged, sorted ranges that I can just get the length 
# to obtain the number of "fresh" IDs

i = 0
merged_ranges = [] # initialise array whe all the merged ranges will go into
# this is going to be a nested list of the form [[min_range1,max_range1],[min_range2,max_range2]]

# start assuming that your first range is going to be the first one of the ordered lists
cur_min_val = ordered_mins[0]
cur_max_val = ordered_maxs[0]

# continue until we have reached the greatest number in the IDs
while cur_max_val<ordered_maxs[-1]:

    # get the minimum value of the next range
    next_min = ordered_mins[i+1]

    # if it overlaps with the current range, update the current max value
    if next_min <= cur_max_val+1:
        cur_max_val = max(cur_max_val, ordered_maxs[i+1]) # choose greatest maximum out of the two ranges 
        # (the one we are currently considering and the next one)

        # print(f"new cur max {cur_max_val}")
    else:
        # if not, "close" this range and make a new oned
        merged_ranges.append([cur_min_val,cur_max_val])
        
        cur_min_val = ordered_mins[i+1]
        cur_max_val = ordered_maxs[i+1]
        # print(f"new min {cur_min_val}")
        # print(f"new max {cur_max_val}")

    i+=1

# append the last range
merged_ranges.append([cur_min_val,cur_max_val])

# # print the obtained ranges
# print(merged_ranges)


# Count the length of all the merged ranges
count = 0
for min_val,max_val in merged_ranges:
    count += max_val+1-min_val

# print result
print(count)