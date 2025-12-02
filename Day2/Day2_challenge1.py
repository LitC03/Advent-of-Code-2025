

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

        len_str = len(str_num)

        # if the string does not have an even amount of digits, it is a valid id
        # So no more investigation is needed
        if not(len_str%2):
            # get the middle index
            middle = int(len_str/2)               
            # compare strings about the middle point
            if str_num[:middle] == str_num[middle:]:
                invalid_ids.append(elem)

# print(invalid_ids)
print(sum(invalid_ids))