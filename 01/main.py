# import pandas as pd
import numpy as np


with open("01/test.txt") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = [int(x) for x in lines[i].strip().split()]

# left vs right
left = []
right = []
for line in lines:
    left.append(line[0])
    right.append(line[1])

# add index to left and right
left = np.array(left)
right = np.array(right)
left = np.column_stack((left, np.arange(len(left))))
right = np.column_stack((right, np.arange(len(right))))

# sort left and right
left = left[left[:, 0].argsort()]
right = right[right[:, 0].argsort()]

print(left)

