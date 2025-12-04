def get_round_coords(y,x,len_x,len_y):
    # yrange will be (y-1,y,y+1) and will be capped at 0 and y_len
    # same for xrange
    y_range = range(max(0, y - 1), min(len_y, y + 2))
    x_range = range(max(0, x - 1), min(len_x, x + 2))

    # make sure to not "check" the center location (x,y)
    where_to_check = [[ny, nx] for ny in y_range for nx in x_range if not (ny == y and nx == x) ]  
    
    return where_to_check

# open the file
f = open("input.txt","r")

# Create a new board where empty spaces are 0s and rolls are 1s
board = []

for line in f:
    chars = line.strip() # strip line
    chars = chars.replace(".","0") # replace empty spaces with 0s
    chars = chars.replace("@","1") # replace rolls with 1s
    int_line = [int(elem) for elem in chars] # cast to ints
    board.append(int_line)

f.close() # close doc

# initialise counter for how many rolls can be removed
count = 0

y_len = len(board)
x_len = len(board[0])

# for every location:
for i in range(y_len):
    for j in range(x_len):

        if board[i][j]: # if there is a 1 (a roll)

             # get the coordinates around it
            coords = get_round_coords(i,j,x_len,y_len)
            # print(f"Position {i},{j}")
            # print(f"Coords around {coords}")

            # collect the values around it
            symbols_around = [board[row][col] for row,col in coords]
            # print(f"Symbols around {symbols_around}")

            # sum all of the 0s and 1s
            total_nums = sum(symbols_around)

            # if there is less than 4 rolls around it, we can remove it
            if total_nums <4:
                # keep count of how many removable rolls there are
                count+=1
                # print("added to count")

# print result
print(count)