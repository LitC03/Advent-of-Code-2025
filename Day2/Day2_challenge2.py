import numpy as np

f = open("input.txt")

line = f.readline() # Read the first line

ranges = line.split(",") # divide the ranges

invalid_ids = [] # initialise an array with all the invalid ids found

for slice in ranges: # for every range:

    # get the low and high limits
    lims = slice.split("-")
    low_lim = int(lims[0])
    high_lim = int(lims[-1])
    # print(f"{low_lim} - {high_lim}")

    # go through every number in that range
    for elem in range(low_lim,high_lim+1):

        # make it a string so I can access every digit individually
        str_num = str(elem)

        # if the id is one digit, it is a valid id
        if len(str_num) == 1:
            continue

        # check if all the elemnts are the same, if yes, it is an invalid id directly
        if all(c == str_num[0] for c in str_num):
            invalid_ids.append(elem)
        
        # if not, divide the string into groups of 2+ elements
        else:
            # the largest group we can make will be the numbers length/2
            middle = int(np.round(len(str_num)/2))
            
            added_id = False
            i = 2

            # for every division of the string in groups of 2,3,4...
            # and as long as we haven't detected an invalid id
            while i<=middle and not(added_id): 

                #get the first group
                first_elem = str_num[0:i]
                # print(f"Fist elem {first_elem}")
                
                #start getting the rest
                # print("Start loop")
                # print(len(str_num))
                for j in range(i,len(str_num),i):
                    str_slice = str_num[j:j+i]
                    # print(f"Elem {str_slice}")
                    # if we realise that the new group is not the same as the first, we break the loop, 
                    # the id is valid according to our slicing
                    if str_slice != first_elem:
                        break
                    # print(j)

                    # if we made it to the ned of the loop and the last element is equal to the first,
                    # we can add the id to our list
                    if j == len(str_num)-i:
                        invalid_ids.append(elem)
                        added_id = True # break the while loop
 
                i+=1

# print(invalid_ids)
print(sum(invalid_ids))