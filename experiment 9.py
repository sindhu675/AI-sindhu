# Travelling Salesman Problem

from itertools import permutations

graph = [[0,10,15,20],
         [10,0,35,25],
         [15,35,0,30],
         [20,25,30,0]]

v = 4
cities = [1,2,3]
min_cost = 999

for p in permutations(cities):
    cost = graph[0][p[0]] + graph[p[0]][p[1]] + graph[p[1]][p[2]] + graph[p[2]][0]
    
    if cost < min_cost:
        min_cost = cost

print("Minimum travelling cost:", min_cost)
