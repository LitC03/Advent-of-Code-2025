import numpy as np
import math

def check_cluster_num(clusters,num):
    for j in range(len(clusters)):
        if num in clusters[j]:
            return j

# open file, read it and close it
f = open("input.txt","r")
lines = f.readlines()
f.close()

# we want to make the first 1000 connections between junction boxes
first_connections = 1000

# initialise a matrix with all the 3d positions
num_jboxes = len(lines)
positions = np.zeros([num_jboxes,3])

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

# sort dict according to its values 
sorted_dict_items = [[k,v] for k, v in sorted(distances.items(), key=lambda item: item[1])]
# print(sorted_dict_items)


# keep track of clusters
clusters = []
# keep tract of what junction boxes have been added
all_vals = []

# i=0

# for the first X connections:
for key,connection in sorted_dict_items[:first_connections]:

    # get what junction boxes we are connecting
    connect = key.split("_")
    # cast them to ints
    connect = [int(elem) for elem in connect]

    # if both junction boxes are already connected somehow
    if all(elem in all_vals for elem in connect):

        # check to which cluster they belong to        
        j = check_cluster_num(clusters,connect[0])
        k = check_cluster_num(clusters,connect[1])

        # if they are in the same cluster, nothing happens
        # if they belong to different clusters, add those clusters together
        # and remove one of them
        if k!=j:
            cluster_to_join = clusters[k].copy() # copy one cluster
            clusters[j].extend(cluster_to_join) # add it to the other
            clusters.remove(cluster_to_join) # remove the copied one

    elif connect[0] in all_vals:
        # if only the first junction box is connected to a cluster, add the other junction box to the cluster
        j = check_cluster_num(clusters,connect[0])
        clusters[j].extend([connect[1]])
        all_vals.extend([connect[1]])

    elif connect[1] in all_vals:
        # if only the second junction box is connected to a cluster, add the other junction box to the cluster
        j = check_cluster_num(clusters,connect[1])
        clusters[j].extend([connect[0]])
        all_vals.extend([connect[0]])
    else:
        # if they don't belong to any cluster, create a new one
        clusters.append(connect)
        all_vals.extend(connect) # and keep track of what junction boxes have at least one connection
    

# get the sorted lengths of every cluster
lengths = [len(elem) for elem in clusters]
lengths.sort(reverse=True)

# print the product of the lengths of the three largest clusters
print(math.prod(lengths[:3]))
