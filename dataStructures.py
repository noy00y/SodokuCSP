class Variable:
    # Initialization
    def __init__(self,name: str,i: int,j: int,value: int,domain: list):
        self.name = name # name of each cord
        self.value = value # assigned value
        self.domain = domain # Domain of the values the list can hold (initiliazed with the CSP Declared variable)
        self.i,self.j = i,j # cord val
        return

    # Debugging
    def __str__(self):
        return f'[{self.i}][{self.j}]'

class CSP:
    def __init__(self):
        self.variables: list = [] # adding all variables to the CSP
        self.edges:list = [] # list of arcs "edge nodes"

    # Adding edge to graph (fromNode, toNode, fromNode Constraints)
    def addArc(self, node1: Variable, node2: Variable, constraint: list):
        self.edges.append([node1,node2,constraint])
        
        # Updating node list with fromNode
        node_exists = False
        for node in self.variables:
            if node1.name==node.name:node_exists = True
        if node_exists==False: self.variables.append(node1)

        return
        

    def view_graph(self): # Print as a list of edges
        print('From|To|Constraint')
        for edge in self.edges:
            print(f'{edge[0].name}|{edge[1].name}|{edge[2]}')
        return    
