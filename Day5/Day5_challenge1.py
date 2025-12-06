f = open("input.txt") # open file and read ir
lines = f.readlines()
f.close() # close it

separation = lines.index("\n") # get index of where the separation 
# happens between ranges and ingredients

# initialise arrays for ingredients and ranges
ingredients = []
mins = []
maxs = []

# read ranges
i = 0
while i<separation: # stop reading lines if we encounter the empty line
    line = lines[i].strip()
    range_vals = line.split("-") # split the ranges into two

    # Cast to int and save ranges
    mins.append(int(range_vals[0])) # save the min values
    maxs.append(int(range_vals[1])) # save the max values of the ranges
    i+=1

# read ingredient list
i = separation+1
while i<len(lines):
    line = lines[i].strip()
    ingredients.append(int(line))
    i+=1
    
# initialise counter for fresh ingredients
count = 0

# for every ingredient:
for ingredient in ingredients:
    # print(f"Ingredient {ingredient}")
    i=0

    for min_val in mins:
        # print(f"min val {min_val}")

        # check if the ingredient is equal or greater
        # than any of the min values of the ranges
        # and equal or less than the correspoinding maximum
        # of that range
        if ingredient>=min_val and ingredient<=maxs[i]:
            #count ingredient as fresh
            count+=1
            # print("added")
            
            # stop looking for apropriate ranges for the ingredient
            break
        i+=1

#print result
print(count)