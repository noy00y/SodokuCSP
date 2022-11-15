# Imports:
from dataStructures import *

# Constants:
DOMAIN = [1,2,3,4,5,6,7,8,9]

"""
Returns list of adjacent board coordinates 
"""
def getAdjacent(board , i, j):
    adjacent = []
    if i!=len(board[0])-1: adjacent.append([f'board[{i+1}][{j}]',i+1,j]) # Append board[i + 1][j] if current node is not in the last row
    if i!=0: adjacent.append([f'board[{i-1}][{j}]',i-1,j])  # Append board[i - 1][j] if current node not in top row
    if j!=len(board)-1: adjacent.append([f'board[{i}][{j+1}]',i,j+1]) # Append board[i][j + 1] (if not right most col)
    if j!=0: adjacent.append([f'board[{i}][{j-1}]',i,j-1]) # Append board[i][j - 1] (if not left most col)
    return adjacent

"""
Constraint Generation
- Box Constraints: 9 constraints
- AllDiff Constraints: 18 Constraints
"""
def get_alldiff_constraints(board,i,j): # Given the puzzle and a cell's index, this function returns the all diff as a binary constraint relative to that cell
    given = (i,j)
    constraints = []
    # Get all the other indexs in the same row and column as a tuple
    for x in range(0,len(board),1):
        if x==i: # if row in itteration==i(row of the element), append that entire row
            for y in range(0,len(board[x]),1):
                if (x,y)!=given: constraints.append(f'board[{i}][{j}]!=board[{x}][{y}]')
        if (x,j)!=given: constraints.append(f'board[{i}][{j}]!=board[{x}][{j}]') 
    return constraints

def get_box_constraints(i,j):
    # Load the box constratins from constraints.txt
    with open('constraints.txt','r') as file: lines=[line.replace('\n','') for line in file.readlines()]
    return [line for line in lines if f'board[{i}][{j}]' in line[0:11]] 

def get_constraints(board,i,j):
    constraints = []
    all_diff_constraints = get_alldiff_constraints(board,i,j)
    for line in all_diff_constraints: constraints.append(line)
    box_constraints = get_box_constraints(i,j)
    for line in box_constraints: constraints.append(line)
    return constraints

"""
Creates a Graph from passed in Board
"""
def createCSP(board: list):
    csp = CSP()

    for i in range(0, len(board)):
        for j in range(0, len(board)):
            
            # Generate Constraints:
            constraints = get_constraints(board, i, j)
            # If value already assigned --> add to constraints
            if board[i][j] != 0: constraints.append(f'board[{i}][{j}]=={board[i][j]}') 
            
            # Create Arcs:
            adjacent = getAdjacent(board, i, j)
            for cord in adjacent: # Create nodes (name, i, j, value, domain)
                from_node = Variable(f'board[{i}][{j}]',i,j,board[i][j],DOMAIN if board[i][j]==0 else [board[i][j]]) # Last field to make sure that the domain for assigned variables is limited to the value assigned to it alone
                to_node = Variable(cord[0],cord[1],cord[2],eval(cord[0]),DOMAIN if board[cord[1]][cord[2]]==0 else board[cord[1]][cord[2]])
                csp.addArc(from_node,to_node,constraints)
                
    return csp

# Test
if __name__ == "__main__":
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
    createGraph(board)