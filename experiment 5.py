# Missionaries and Cannibals Problem

visited = set()

def solve(m, c, boat):
    if (m, c, boat) in visited:
        return False

    visited.add((m, c, boat))

    if m == 0 and c == 0:
        print("Goal Reached")
        return True

    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]

    for x,y in moves:
        if boat == 1:
            nm = m - x
            nc = c - y
            nb = 0
        else:
            nm = m + x
            nc = c + y
            nb = 1

        if 0 <= nm <= 3 and 0 <= nc <= 3:
            if solve(nm, nc, nb):
                print("State:", nm, nc, nb)
                return True

    return False

solve(3,3,1)
