# Simple Feed Forward Neural Network

import math

# sigmoid activation function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# inputs
x1 = 0.5
x2 = 0.8

# weights
w1 = 0.2
w2 = 0.4
w3 = 0.3
w4 = 0.7

# hidden layer
h1 = sigmoid(x1*w1 + x2*w2)
h2 = sigmoid(x1*w3 + x2*w4)

# output layer
w5 = 0.6
w6 = 0.9
output = sigmoid(h1*w5 + h2*w6)

print("Output of Feed Forward Neural Network:", output)
