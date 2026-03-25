# Map Coloring Problem using CSP

states = ['A','B','C','D']

neighbors = {
'A': ['B','C'],
'B': ['A','C','D'],
'C': ['A','B','D'],
'D': ['B','C']
}

colors = ['Red','Green','Blue']

solution = {}

def safe(state, color):
    for n in neighbors[state]:
        if n in solution and solution[n] == color:
            return False
    return True

def solve():
    for state in states:
        for color in colors:
            if safe(state, color):
                solution[state] = color
                break

solve()

for s in solution:
    print(s, ":", solution[s])
