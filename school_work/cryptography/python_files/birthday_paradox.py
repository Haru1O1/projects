import math

def birthday_run(B, P):
    M = 2**B
    num_messages = math.ceil(math.sqrt(2 * M * math.log(1 / (1-P))))
    print("Number of messages needed:", num_messages)

# output bits length
B = 8

# number of possible outputs
M = 2**B

# collision probability
P = 0.1

num_messages = math.ceil(math.sqrt(2 * M * math.log(1 / (1-P))))
print("Number of messages needed:", num_messages)
