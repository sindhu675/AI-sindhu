# Alpha-Beta Pruning Algorithm

def alphabeta(depth, alpha, beta, isMax):
    
    if depth == 0:
        return 3   # example value

    if isMax:
        value = -100
        for i in range(2):
            value = max(value, alphabeta(depth-1, alpha, beta, False))
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value

    else:
        value = 100
        for i in range(2):
            value = min(value, alphabeta(depth-1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value


result = alphabeta(3, -100, 100, True)
print("Best value:", result)
