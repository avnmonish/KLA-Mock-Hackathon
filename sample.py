
import json


def tsp_dp(distance_matrix):
    n = len(distance_matrix)
    all_points_set = set(range(n))
    memo = {}

    def tsp_dp_helper(current, remaining):
        if not remaining:
            return distance_matrix[current][0]  # Return to starting point (0)

        if memo != {} and (current, remaining) in memo:
            print('hai')
            return memo[(current, remaining)]

        print('current', current, remaining)
        min_distance = float('inf')
        for next_point in remaining :
            new_remaining = remaining - {next_point}
            distance = distance_matrix[current][next_point] + tsp_dp_helper(next_point, new_remaining)
            min_distance = min(min_distance, distance)

        print('min', min_distance)
        memo[(current, remaining)] = min_distance
        return min_distance

    return tsp_dp_helper(0, all_points_set - {0})

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

shortest_path_distance = tsp_dp(dist)
print("Shortest path distance:", shortest_path_distance)