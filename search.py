# Imports
from dataStructures import *
import copy

def revise(arc, board: list):
    print("-------------------------------------------------")
    print(f"Calling Revise on the Arc: {arc[0]} and {arc[1]}")
    
    # Declarations
    revised = False
    Xi = copy.deepcopy(arc[0])
    domainX = copy.deepcopy(Xi.domain)
    print(f'domainX before trim: {domainX}')
    constraintsX = copy.deepcopy(arc[2]) 
    cordVal = copy.deepcopy(Xi.value) 
    removeVals = []

    # Change domainX to list if not already:
    if isinstance(domainX, int):
        domainX = list(map(int, str(domainX)))

    # Trimming Xi Domain
    for domain in domainX:
        print(f'[{Xi.i}][{Xi.j}] = {domain}')
        board[Xi.i][Xi.j] = domain # temp storing for evaluation
        
        # Constraint Iteration
        iteration = True
        counts = 0
        
        # While constraint not broken otherwise loop to next domainX
        while iteration and counts < len(constraintsX):
            c = constraintsX[counts]
            if eval(c) == False:
                if domain in domainX:
                    print(f'{c} --> remove {domain}')
                    temp = domain
                    removeVals.append(domain)
                    revised = True
                    iteration = True

            # Increment counts for iteration
            counts += 1 

    for val in removeVals:
        if val in domainX:
            domainX.remove(val)
    

    # If domain was trimmed --> trim og domain
    if revised:
        arc[0].domain = copy.deepcopy(domainX)

    board[Xi.i][Xi.j] = cordVal
    print(f'domainX after trim: {domainX}')
    return revised
 
def AC3(csp: CSP, board: list):
    print("----------------AC3-----------------")
    queue: list = [edge for edge in csp.edges] # load edges into the "queue"
    
    # AC3 Loop
    while len(queue) > 0:
        arc = queue.pop() # (Node1 <--> Node2)
        # print(f'Arc Popped: [{arc[0].i}][{arc[0].j}] <--> [{arc[1].i}][{arc[1].j}]')
        if revise(arc, board): 
            if(len(arc[0].domain) == 0): return False # CSP has failed --> backtrack
            for edge in csp.edges:
                # print(f'[{arc[0].i}][{arc[0].j}] >>> [{edge[0].i}][{edge[0].j}] <--> [{edge[1].i}][{edge[1].j}]', end = " --> ")
                if arc[1].i!=edge[0].i and arc[1].j!=edge[0].j and arc[0].i == edge[1].i and arc[0].j == edge[1].j:
                    # print("Edge Found")
                    queue.append(edge)
                # else: print("This is not the edge")
        # else: 
        #     print(f'No Revision: [{arc[0].i}][{arc[0].j}] <--> [{arc[1].i}][{arc[1].j}]')
        
    return True # Arc Consistent

def backtrack():
    pass

def backtrackAux():
    pass
