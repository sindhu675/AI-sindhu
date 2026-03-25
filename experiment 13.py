# Simple Minimax Algorithm

def minimax(depth, isMax):
    if depth == 0:
        return 0

    if isMax:
        best = -100
        for i in range(2):
            val = minimax(depth-1, False)
            best = max(best, val)
        return best
    else:
        best = 100
        for i in range(2):
            val = minimax(depth-1, True)
            best = min(best, val)
        return best

result = minimax(3, True)
print("Best value:", result)
