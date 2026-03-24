# 8 Puzzle Problem

def display(p):
    for i in p:
        print(i)
    print()

def move(p, x1, y1, x2, y2):
    p[x1][y1], p[x2][y2] = p[x2][y2], p[x1][y1]

# Initial state
p = [[1,2,3],
     [4,0,6],
     [7,5,8]]

print("Initial State")
display(p)

# Move blank down
move(p,1,1,2,1)
print("Step 1")
display(p)

# Move blank right
move(p,2,1,2,2)
print("Goal State")
display(p)
