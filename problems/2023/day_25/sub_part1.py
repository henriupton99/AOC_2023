import networkx as nx
FILENAME = "input.txt"
lines = [line.replace(":","").split(" ") for line in open(FILENAME).read().splitlines()]

# Create a directionnal graph 
# as our case is undirectionnal, just need to add 2 nodes parent->child, child->parent
graph = nx.DiGraph()
for line in lines:
    parent = line[0]
    for child in line[1:]:
        graph.add_edge(parent,child,capacity=1.0)
        graph.add_edge(child,parent,capacity=1.0)

# Go though all the nodes and find minimum cut and partition
# we know we search for a 3 num_cuts partition
for line in lines:
    parent = line[0]
    for child in line[1:]:
        cut_value, partition = nx.minimum_cut(graph,parent,child)
        if cut_value == 3:
            print(len(partition[0])*len(partition[1]))
            break