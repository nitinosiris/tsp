import random
import sys

NUM_NODES = int(sys.argv[1])

f = open(f"input{NUM_NODES}.txt", "w")

# f.write(f"{NUM_NODES}\n")

for i in range(1,NUM_NODES+1):

    for j in range(i+1,NUM_NODES+1):

        wt = random.randint(1, 100)
        
        f.write(f"{i} {j} {wt}\n")

f.close()