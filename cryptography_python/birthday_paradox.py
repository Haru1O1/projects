import math

# output bits length
B = 8

# number of possible outputs
M = 2**B

# collision probability
P = 0.1

num_messages = math.ceil(math.sqrt(2 * M * math.log(1 / (1-P))))
print("Number of messages needed:", num_messages)
