
'''
Problem statement
Steve has worked as Chef in many star hotels in multiple continents. Steve aspires 
to set up a chain of restaurants in his hometown Coimbatore. Steve figures starting 
with a cloud kitchen might be the first logical step. Steve after talking to his friends 
has identified three areas as potential places to start his business - RS Puram, 
Saibaba Colony and Peelamedu. Steve has hired a consultant to help narrow down 
to location and also type of food / restaurant business to start. Steve is very excited 
to start a Pastry based Restaurant.


Level 0
Consultant has mapped Saibaba colony into 20 neighborhoods and also 
suggested location for first Restaurant / cloud kitchen. Steve wants to start from 
the restaurant and cover all neighborhoods and return to the restaurant using the 
shortest possible path avoiding already visited neighborhoods. So we want to write 
a program that can recommend the path Steve needs to traverse to generate 
outfile.

'''

import json

# Reading
with open('level0.json', 'r') as file :
    code = json.load(file)  # Gives a dict.

# Neighbourhood Distances :
r0 = code['restaurants']['r0']['neighbourhood_distance']

n0 = code['neighbourhoods']['n0']['distances']
n1 = code['neighbourhoods']['n1']['distances']
n2 = code['neighbourhoods']['n2']['distances']
n3 = code['neighbourhoods']['n3']['distances']
n4 = code['neighbourhoods']['n4']['distances']

n5 = code['neighbourhoods']['n5']['distances']
n6 = code['neighbourhoods']['n6']['distances']
n7 = code['neighbourhoods']['n7']['distances']
n8 = code['neighbourhoods']['n8']['distances']
n9 = code['neighbourhoods']['n9']['distances']

n10 = code['neighbourhoods']['n10']['distances']
n11 = code['neighbourhoods']['n11']['distances']
n12 = code['neighbourhoods']['n12']['distances']
n13 = code['neighbourhoods']['n13']['distances']
n14 = code['neighbourhoods']['n14']['distances']

n15 = code['neighbourhoods']['n15']['distances']
n16 = code['neighbourhoods']['n16']['distances']
n17 = code['neighbourhoods']['n17']['distances']
n18 = code['neighbourhoods']['n18']['distances']
n19 = code['neighbourhoods']['n19']['distances']

# Distance matrix :
dist = [n0, n1, n2, n3, n4,
        n5, n6, n7, n8, n9,
        n10, n11, n12, n13, n14,
        n15, n16, n17, n18, n19]

# Function to find the nearest neighbor :
def nearest_neighbor(current_node, unvisited_nodes) :
    return min(unvisited_nodes, key = lambda x : dist[current_node][x])

path = []  # Stores the path
unvisited = list(range(20))


path += [r0.index(min(r0))]
unvisited.remove(path[-1])
pathCost = [min(r0)]
pathSum = pathCost[-1]

while unvisited :
    closest = nearest_neighbor(path[-1], unvisited)
    path += [closest]
    unvisited.remove(closest)


print('\nNeighbour Distances : ')
for i in range(len(dist)) :
    print('dis ', i, ' : ', dist[i])
print()

print('r0 : ', r0)

print()
print('\nDesired path :')
print(path)






# cost of each traversal :
for i in range(19) :
    pathCost += [dist[path[i]][path[i + 1]]]
    pathSum += pathCost[-1]
pathSum += r0[path[-1]]
pathCost += [r0[path[-1]]]

print('\nPath cost :')
print(pathCost)
print('\nPath sum : ', pathSum, '\n')


# Path with name :
namepath = ['r0']
for i in range(len(path)) :
    namepath += ['n' + str(path[i])]
namepath += ['r0']

# Final ans :
ans = {'v0' : {'path' : namepath}}
print(ans)

with open('level0_output.json', 'w') as file :
    json_str = json.dumps(ans)
    file.write(json_str)
