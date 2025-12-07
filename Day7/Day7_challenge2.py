# open the document, read it and close it
f = open("input.txt")
lines = f.readlines()
f.close()

# count the number of lines and characters in each line
num_cols = len(lines[0].strip())
nums_rows = len(lines)

# Keep count of how many timelines there are in each column
beams = [0]*num_cols
index_S = lines[0].index("S")
beams[index_S]+=1 # add the initial beam

# read all lines (expcept the last one because it is all dots)
for i in range(1,nums_rows-1):
    # read the line:
    line = lines[i]

    # find every occurrence of a beamsplitter    
    splitter_pos = [i for i in range(len(line)) if line.startswith("^", i)]

    # if there is none, continue to next line
    if not(len(splitter_pos)):
        continue
    # print(splitter_pos)

    # create a copy of the old line
    new_line = beams.copy()

    # for every beamsplitter:
    for beam_split in splitter_pos:
        # if a beam hit it:
        if beams[beam_split]:
            # there wont be a beam directly under the beamsplitter
            new_line[beam_split] = 0
            # but on every side of it, there will be a new time line
            # equal to the timelines that hit the beamsplitter
            new_line[beam_split-1]+=beams[beam_split]
            new_line[beam_split+1]+=beams[beam_split]

    # the new line now becomes the old line
    beams = new_line.copy()

# print the total amount of timelines from the last iteration
print(sum(beams))