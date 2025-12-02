f = open("input.txt","r")
prev_pos = 50
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

    new_pos = prev_pos + steps # calculate the new position after rotation

    # initialise "pass by zero" counter to 0
    add = 0 
    
    # if we end up in a number above 99 (in any direction) we must have passed zero
    add = abs(new_pos) // 100

    # if we end up in zero, count that
    if not(new_pos):
        add+=1
    
    # if we cross zero by going to negative numbers, count that too. 
    # Make sure you don't count zero twice if you started at 0
    if prev_pos != 0 and new_pos <0:
        add+=1
    
    # print(f"added {add}")
    count+=add

    #get the actual new position by taking the remainder of dividing by 100
    new_pos = new_pos % 100 

    prev_pos = new_pos

print(count)

f.close()