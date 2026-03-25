# A* Algorithm

graph = {
'A': ['B','C'],
'B': ['D'],
'C': ['E'],
'D': [],
'E': []
}

h = {'A':4,'B':2,'C':3,'D':0,'E':0}

open_list = ['A']
visited = []

while open_list:
    n = open_list.pop(0)
    print(n, end=" ")
    visited.append(n)

    for i in graph[n]:
        if i not in visited:
            open_list.append(i)
