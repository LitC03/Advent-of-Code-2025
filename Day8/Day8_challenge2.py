import numpy as np


# open file, read it and close it
f = open("input.txt","r")
lines = f.readlines()
f.close()

# initialise a matrix with all the 3d positions
num_jboxes = len(lines)
positions = np.zeros([num_jboxes,3],dtype=int)

i=0
for line in lines:
    x,y,z = line.strip().split(",")
    positions[i,:] = [int(x),int(y),int(z)]
    i+=1

# keep track of the distances between all the junction boxes with a dict
distances = dict()

i = 0
for pos in positions:
    # avoid repeated distances (so do not have distance0_1 and distance1_0)
    for j in range(i+1,num_jboxes):

        key = str(i)+"_"+str(j) # the key of the entry will be of the form 
        # "0_1" meaning it is the distance between junction box 0 and junction box 

        # calculate the distances and add them to the dictionary
        distances[key] = int(sum((pos - positions[j,:])**2)) # no need to take the square root because the square root is a monotonic function
    i+=1

# print(distances)

# sort the keys of the distances dict according to its values 
sorted_keys = [k for k, _ in sorted(distances.items(), key=lambda item: item[1])]

# keep tract of what junction boxes have been added
all_vals = set()

i=0

# keep track of all the unique values of juncion boxes that have been connected
# and stop when all boxes have been connected
while len(all_vals)<num_jboxes:
    # see what junction boxes we are connecting
    key = sorted_keys[i]
    connect = key.split("_")
    all_vals.update(connect)  # update set (that contains unique values only)
    i+=1

# get the x coordinates of the last connected junction boxes
x1 = positions[int(connect[0]),0]
x2 = positions[int(connect[1]),0]

# print results
print(f"X coordinates of the junctions that produce one giant circuit: {x1},{x2}")
print(f"Their product: {x1*x2}")
