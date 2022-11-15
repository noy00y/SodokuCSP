# Imports:
from dataStructures import *
from search import *
from board import createCSP
import numpy as np

# Constants:
DOMAIN = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board = [
    [4,8,3, 9,2,1, 6,5,7],
    [9,6,0, 3,4,5, 8,0,1],
    [2,5,1, 8,7,6, 4,9,3],

    [5,4,8, 1,3,2, 9,7,6],
    [7,2,9, 5,0,0, 1,3,8],
    [1,0,6, 7,9,8, 2,0,5],

    [3,7,2, 6,8,9, 5,1,4],
    [0,1,0, 2,5,3, 7,6,9],
    [6,9,5, 4,1,7, 0,8,2],
]

# Initialization:
csp = createCSP(board)
print(f'Unsolved State: \n{np.array(board)}')
print("------------------------------------")
# Call AC3 and begin Trimming:
if AC3(csp, board):
    for n in csp.variables:
        node: Variable = n
        print(f'Assign: {node.domain} for [{node.i}][{node.j}]')
        if len(node.domain) == 1: # assign node
            # print(f'Assign: {node.domain[0]} for [{node.i}][{node.j}]')
            board[node.i][node.j] = node.domain[0]
            node.value = node.domain[0]

    print("------------------------------------")
    print(f'Solved State: \n{np.array(board)}')
    

else:
    print("that nigga failed") 