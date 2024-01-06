'''
Problem statement
Steve has worked as Chef in many star hotels in multiple continents. Steve aspires 
to set up a chain of restaurants in his hometown Coimbatore. Steve figures starting 
with a cloud kitchen might be the first logical step. Steve after talking to his friends 
has identified three areas as potential places to start his business - RS Puram, 
Saibaba Colony and Peelamedu. Steve has hired a consultant to help narrow down 
to location and also type of food / restaurant business to start. Steve is very excited 
to start a Pastry based Restaurant.

Level 1a
Steve after walking thru the location is confident about prospects of pastry 
business in Saibaba colony and has finalized the location of Pastry cloud kitchen. 
Steve is very risk averse so Steve advertised pre-order for Pastry to be delivered 
as evening snack. Steve has hired one delivery person and has a scooter with a 
modified carrier. Based on the day's orders he wants to communicate the delivery 
slots to his customers. Since the scooter carrier has finite capacity and customers 
may order cupcakes, birthday cake, bread etc We are tasked with writing a 
program that will allow Steve to enter all orders for the day and we create different 
slots. We want to make sure we can fill the scooter carrier to max possible capacity 
and also conserve petrol by making each drop slot cover a minimum distance. 
Goal is reduce number trips and total distance traveled
'''

import json

# Reading
with open('level1b.json', 'r') as file :
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
unvisited = list(range(50))


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

print('len', len(path))

# cost of each traversal :
for i in range(49) :
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

''''''
# Final ans :
ans = {'v0' : {'path' : namepath}}
print(ans)


############# 2 ###########

# Capacity of scooter.
cap = code['vehicles']['v0']['capacity']  #600

# Order quantities :
q0 = code['neighbourhoods']['n0']['order_quantity']
q1 = code['neighbourhoods']['n1']['order_quantity']
q2 = code['neighbourhoods']['n2']['order_quantity']
q3 = code['neighbourhoods']['n3']['order_quantity']
q4 = code['neighbourhoods']['n4']['order_quantity']

q5 = code['neighbourhoods']['n5']['order_quantity']
q6 = code['neighbourhoods']['n6']['order_quantity']
q7 = code['neighbourhoods']['n7']['order_quantity']
q8 = code['neighbourhoods']['n8']['order_quantity']
q9 = code['neighbourhoods']['n9']['order_quantity']

q10 = code['neighbourhoods']['n10']['order_quantity']
q11 = code['neighbourhoods']['n11']['order_quantity']
q12 = code['neighbourhoods']['n12']['order_quantity']
q13 = code['neighbourhoods']['n13']['order_quantity']
q14 = code['neighbourhoods']['n14']['order_quantity']

q15 = code['neighbourhoods']['n15']['order_quantity']
q16 = code['neighbourhoods']['n16']['order_quantity']
q17 = code['neighbourhoods']['n17']['order_quantity']
q18 = code['neighbourhoods']['n18']['order_quantity']
q19 = code['neighbourhoods']['n19']['order_quantity']

#print(q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19)

Q = [q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19]
print('sum', sum(Q))

path += [-1]
disPath = []

for i in range(51) :
    disPath += [[pathCost[i], path[i]]]

disPath.sort()

print('Dispath')
print(disPath)

pathCount = []
tmpC = 0
costs = []
start = 0

for i in range(len(disPath)) :
    if tmpC + Q[disPath[i][1]] > cap :
        pathCount += [disPath[start : i]]
        costs += [tmpC]
        start = i
        tmpC = Q[disPath[i][1]]

    else :
        tmpC += Q[disPath[i][1]]


print('\n\ndetails\n')
for i in range(len(pathCount)) :
    print(pathCount[i])
print()

for i in range(len(costs)) :
    print(costs[i])
print()

# Extract path.
nodes = []
tmpList = []

for i in range(len(pathCount)) :

    tmpList = ["r0"]
    for j in range(len(pathCount[i])) :
        tmpList += ["n" + str(pathCount[i][j][1])]
    
    tmpList += ["r0"]

    nodes += [tmpList]
    

print(tmpList)
print(nodes)


count = 0
final = {"v0" : {}}

for i in range(len(nodes)) :
    final['v0']['path' + str(i + 1)] = nodes[i]

print(final)

with open('level1a_output.json', 'w') as file :
    json_str = json.dumps(final)
    file.write(json_str)

'''
Q :
70 70 90 50 70 90 110 70 110 70 70 110 110 90 50 90 110 90 70 110
'''


























