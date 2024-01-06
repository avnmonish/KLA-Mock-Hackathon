
import json


def tsp_dp(distance_matrix):
    n = len(distance_matrix)
    all_points_set = frozenset(range(n))  # Use frozenset for hashing
    memo = {}

    def tsp_dp_helper(current, remaining):
        if not remaining:
            return distance_matrix[current][0], [0]  # Return distance and path [0] indicates starting point

        if (current, tuple(remaining)) in memo:
            return memo[(current, tuple(remaining))]

        min_distance = float('inf')
        min_path = None

        for next_point in remaining:
            new_remaining = remaining - {next_point}
            distance, path = tsp_dp_helper(next_point, new_remaining)
            total_distance = distance_matrix[current][next_point] + distance

            if total_distance < min_distance:
                min_distance = total_distance
                min_path = [current] + path

        memo[(current, tuple(remaining))] = min_distance, min_path
        return min_distance, min_path

    distance, path = tsp_dp_helper(0, all_points_set - {0})
    return distance, path









# Reading
with open('level0.json', 'r') as file :
    code = json.load(file)  # Gives a dict.

# Neighbourhood Distances :
r0 = [0] + code['restaurants']['r0']['neighbourhood_distance']

n0 = [r0[1]] + code['neighbourhoods']['n0']['distances']
n1 = [r0[2]] + code['neighbourhoods']['n1']['distances']
n2 = [r0[3]] +  code['neighbourhoods']['n2']['distances']
n3 = [r0[4]] +  code['neighbourhoods']['n3']['distances']
n4 = [r0[5]] +  code['neighbourhoods']['n4']['distances']

n5 = [r0[6]] +  code['neighbourhoods']['n5']['distances']
n6 = [r0[7]] +  code['neighbourhoods']['n6']['distances']
n7 = [r0[8]] +  code['neighbourhoods']['n7']['distances']
n8 = [r0[9]] +  code['neighbourhoods']['n8']['distances']
n9 = [r0[10]] +  code['neighbourhoods']['n9']['distances']

n10 = [r0[11]] +  code['neighbourhoods']['n10']['distances']
n11 = [r0[12]] +  code['neighbourhoods']['n11']['distances']
n12 = [r0[13]] +  code['neighbourhoods']['n12']['distances']
n13 = [r0[14]] +  code['neighbourhoods']['n13']['distances']
n14 = [r0[15]] +  code['neighbourhoods']['n14']['distances']

n15 = [r0[16]] +  code['neighbourhoods']['n15']['distances']
n16 = [r0[17]] +  code['neighbourhoods']['n16']['distances']
n17 = [r0[18]] +  code['neighbourhoods']['n17']['distances']
n18 = [r0[19]] +  code['neighbourhoods']['n18']['distances']
n19 = [r0[20]] +  code['neighbourhoods']['n19']['distances']

# Distance matrix :
distance_matrix = [r0, n0, n1, n2, n3, n4,
        n5, n6, n7, n8, n9,
        n10, n11, n12, n13, n14,
        n15, n16, n17, n18, n19]

shortest_path_distance, shortest_path = tsp_dp(distance_matrix)
print("Shortest path distance:", shortest_path_distance)
print("Shortest path:", shortest_path)

namepath = []
for path in shortest_path :
    if path == 0 :
        namepath += ["r0"]
    else :
        namepath += [str(path - 1)]

ans = {'v0' : {'path' : namepath}}
print(ans)


['r0', 'n3', 'n16', 'n1', 'n18', 'n2', 'n14', 'n9', 'n12', 'n10', 'n15', 'n4', 'n17', 'n7',
 'n19', 'n6', 'n5', 'n0', 'n11', 'n8', "n13", 'r0']
