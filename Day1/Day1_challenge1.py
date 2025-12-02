f = open("input.txt","r")
pos = 50
count = 0
# print(f"Position {pos}")

# Read every line of the input
for line in f:
    direction = line[0] # the first element is the direction of rotation
    # print(f"Direction: {dir}")

    steps = int(line[1:].split("\n")[0]) # obtain the number os steps that will be made in that direction
    # print(f"Steps {steps}")

    if direction == "L": # if we are going left we are making "negative" steps
        steps = - steps
   
    new_pos = pos + steps # calculate the new position after rotation
    # print(f"New position {new_pos}")

    # get the actual new position by taking the remainder of dividing by 100
    new_pos = new_pos % 100 
    
    # if we end up in zero, count that
    if not(new_pos):
        count+=1

    pos = new_pos
    # print(f"Position {pos}")

print(count)
        