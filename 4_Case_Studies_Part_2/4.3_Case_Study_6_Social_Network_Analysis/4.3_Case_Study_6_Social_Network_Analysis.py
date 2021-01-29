########################################
# 4.3.1 INTRODUCTION TO NETWORK ANALYSIS
########################################
# Systems consist of interacting components: Nodes (Vertices) = Components; Edges (Links)= Interactions

# Network = Real world object
# Graph = Abstract mathematical representation

# Neighbours = Linked vertices
# Degree = Number of entries connected to it
# Path = Sequence of unique vertices
# Length = Number of edges in the path
# Component = Pieces of connected nodes (if graph is disconnected)
# Size = Number of nodes in a component

###############################################
# 4.3.1 INTRODUCTION TO NETWORK ANALYSIS - Quiz
###############################################
# Question 1: What is a path in a network?
# Solution 1: A sequence of edges connecting two nodes

# Question 2: What is a connected component in a network?
# Solution 2: A group of nodes and their edges for which a path exists between each node in the component

##########################
# 4.3.2 BASICS OF NETWORKX
##########################
# Networks are created & manipulated by NetworkX module
import networkx as nx
G = nx.Graph() # Create an empty graph
G.add_node(1) # Add single node top graph
G.add_nodes_from([2,3]) # Add multiple nodes - must be in a list
G.add_nodes_from(["u","v"]) # Doesn't have to be numbers
G.nodes() # See the nodes in our graph
G.add_edge(1,2) # Use node labels as input arguments
G.add_edge("u","v") # Use node labels as input arguments
G.add_edges_from([(1,3), (1,4), (1,5), (1,6)]) # Must be a list that consists of tuples - nodes don't have to exist
G.add_edge("u", "w") # Python adds nodes automatically
G.edges() # See edges in graph
G.remove_node(2) # Can remove nodes from graph
G.nodes() # Node 2 has disappeared
G.edges() # Edge (1, 2) has disappeared
G.remove_nodes_from([4,5]) # Can remove multiple nodes - must be a list
G.nodes() # Nodes 4 & 5 are gone
G.remove_edge(1,3) # Can remove edges without removing nodes
G.edges() # Edge (1, 3) has disappeared
G.nodes() # Nodes 1 & 3 remain
G.remove_edges_from([(1,2), ("u","v")]) # Can remove multiple edges - list of tuples
G.edges() # Returns "EdgeView([(1, 6), ('u', 'w')])"
G.number_of_edges() # Returns "2"
G.number_of_nodes() # Returns "6"

#################################
# 4.3.2 BASICS OF NETWORKX - Quiz
#################################
# Question 1: Consider the following code:
#               G = nx.Graph()
#               G.add_nodes_from(1,2,3,4)
#               G.add_edges_from((1,2),(3,4))
#               G.number_of_nodes(), G.number_of_edges()
#             What does this return?
# Solution 1: Those code contains an error = add_nodes_from and add_edges_from take only a single iterable argument each

###########################
# 4.3.3 GRAPH VISUALISATION
###########################
# Let's use empirical data set Karate Club Graph - Nodes = Members; Edges = Friendships
G = nx.karate_club_graph() # Extract data & assign to object 'G'
import matplotlib.pyplot as plt
nx.draw(G) # Visualise network - basically useless without labels
nx.draw(G, with_labels=True) # We want colour!
nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray") # Cool!
plt.savefig("karate_graph.png")

# NetworkX stores the degrees of nodes in a dictionary - Keys = Node IDs; Values = Associated Degrees
G.degree() # Access dictionary
G.degree()[33] # Find degree of given node - Returns "17" - Return a dictionary
G.degree(33) # Find degree of given node - Returns "17" - Use function to look up in the dictionary

##################################
# 4.3.3 GRAPH VISUALISATION - Quiz
##################################
# Question 1: How many nodes and edges are included in the karate club network (as described in Video 4.3.3)?
# Solution 1:
              G.number_of_nodes(), G.number_of_edges() # Answer = 34 nodes, 78 edges

# Question 2: What does G.degree(0) is G.degree()[0] return?
# Solution 2: True

# Question 3: Which function in networkx (imported as nx) plots a network?
# Solution 3: nx.draw

#####################
# 4.3.4 RANDOM GRAPHS
#####################
# Erdos-Renyi (ER) Graph model = simplest random graph model
# 2 Parameters: N = Number of nodes; p = probability of an pair of nodes to be connected

# Let's write an ER function:
from scipy.stats import bernoulli # For probability coin flip
bernoulli.rvs(p=0.2) # Random variable with a 20% chance that it's a 1 (80% chance it's a 0)
N = 20
p = 0.2
G = nx.Graph() # Create empty graph
G.add_nodes_from(range(N)) # Add all N nodes in graph
for node1 in G.nodes(): # Loop over all pairs of nodes
    for node2 in G.nodes(): # Loop over all pairs of nodes
        if bernoulli.rvs(p=p): # With probability 'p', if we get a 1,
            G.add_edge(node1, node2) # Add an edge between nodes
G.number_of_nodes() # Returns "20" - N = 20
nx.draw(G) # We are clearly considering each pair twice (as (1,2) and then as (2,1))
# Modify code:
G = nx.Graph() # Create empty graph
G.add_nodes_from(range(N)) # Add all N nodes in graph
for node1 in G.nodes(): # Loop over all pairs of nodes
    for node2 in G.nodes(): # Loop over all pairs of nodes
        if node1 < node2 and bernoulli.rvs(p=p): # With probability 'p', if we get a 1, - MODIFICATION = only if 1 < 2
            G.add_edge(node1, node2) # Add an edge between nodes
nx.draw(G) # Graph is far less dense & now correct!
# Turn this into a function:
def er_graph(N, p): # N & p as parameters/arguments
    """Generate an ER graph."""
    G = nx.Graph() # Create empty graph
    G.add_nodes_from(range(N)) # Add all N nodes in graph
    for node1 in G.nodes(): # Loop over all pairs of nodes
        for node2 in G.nodes(): # Loop over all pairs of nodes
            if node1 < node2 and bernoulli.rvs(p=p): # With probability 'p', if we get a 1,
                G.add_edge(node1, node2) # Add an edge between nodes
    return G # Return the graph
nx.draw(er_graph(50, 0.08), node_size=40, node_color="gray")
plt.savefig("er1.png")

############################
# 4.3.4 RANDOM GRAPHS - Quiz
############################
# Question 1: How many components do you expect in an Erdős-Rényi graph with n=10 and p=1?
# Solution 1: 1 - p=1 means an edge exists between each node pair, making the network consist of one component.

# Question 2: How many components do you expect in an Erdős-Rényi graph with n=10 and p=0?
# Solution 2: 10 - p=0 means the network will contain no edges, so each node is also its own component.

########################################
# 4.3.5 PLOTTING THE DEGREE DISTRIBUTION
########################################
# Let's plot the degree distribution graph:
def plot_degree_distribution(G):
    degree_sequence = [d for n, d in G.degree()] # Look at the degrees - we want the values (i.e. degrees)
    plt.hist(degree_sequence, histtype="step") # Draw histogram
    plt.xlabel("Degree $k$") # $ around k allows k to be rendered as LaTeX
    plt.ylabel("$P(k)") # y = probability of k
    plt.title("Degree Distribution")

plt.style.use("bmh")
G1 = er_graph(500, 0.08)
plot_degree_distribution(G1)
G2 = er_graph(500, 0.08)
plot_degree_distribution(G2)
G3 = er_graph(500, 0.08)
plot_degree_distribution(G3)
plt.savefig("hist_3.png")

###############################################
# 4.3.5 PLOTTING THE DEGREE DISTRIBUTION - Quiz
###############################################
# Question 1: Consider the following code:
#               D = {1:1, 2:2, 3:3}
#               plt.hist(D)
#             What will this plot?
# Solution 1: Apparently "This code contains an error." because "plt.hist does not take dictionaries a single argument."

# Question 2: How do the degree distributions in nx.erdos_renyi_graph(100, 0.03) and nx.erdos_renyi_graph(100, 0.30)
#             compare?
# Solution 2: The latter distribution has a greater mean on average.

###########################################################
# 4.3.6 DESCRIPTIVE STATISTICS OF EMPIRICAL SOCIAL NETWORKS
###########################################################
# Adjacency Network:
# N nodes = N by N matrix
# Entry ij =1 if node i & node j have a tie between them, otherwise entry = 0
# ij = ji

# Village Relationships in India:
import numpy as np
A1 = np.loadtxt("adj_allVillageRelationships_vilno_1.csv", delimiter=",") # Load in data from village 1
A2 = np.loadtxt("adj_allVillageRelationships_vilno_2.csv", delimiter=",") # Load in data from village 2
G1 = nx.to_networkx_graph(A1) # Convert A1 to NetworkX object 'G1'
G2 = nx.to_networkx_graph(A2) # Convert A2 to NetworkX object 'G2'
# Make a function that prints the basic stats of network
def basic_net_stats(G):
    print("Number of Nodes: %d" % G.number_of_nodes())
    print("Number of Edges: %d" % G.number_of_edges())
    degree_sequence = [d for n, d in G.degree()]
    print("Average Degree: %.2f" % np.mean(degree_sequence))
basic_net_stats(G1) # Returns "Number of Nodes: 843
                             # Number of Edges: 3405
                             # Average Degree: 8.08"
basic_net_stats(G2) # Returns "Number of Nodes: 877
                             # Number of Edges: 3063
                             # Average Degree: 6.99"
plt.style.use("bmh")
plot_degree_distribution(G1)
plot_degree_distribution(G2)
plt.savefig("village_hist.png")
# It seems ER graphs are very different from these real-world graphs, so do not realistically represent rea-world data


##################################################################
# 4.3.6 DESCRIPTIVE STATISTICS OF EMPIRICAL SOCIAL NETWORKS - Quiz
##################################################################
# Question 1: As described in Video 4.3.6, which network has more nodes?
# Solution 1: G2

# Question 2: As described in Video 4.3.6, which network has more edges?
# Solution 2: G1

###############################################
# 4.3.7 FINDING THE LARGEST CONNECTED COMPONENT
###############################################
# nx.connected_component_subgraphs = Extract components from a graph
# ^^^ This was deprecated with 2.1 & removed with 2.4 - Use (G.subgraph(c) for c in nx.connected_components(G))
gen = (G1.subgraph(c) for c in nx.connected_components(G1)) # Is a generator object
g = gen.__next__() # Is a network graph
g.number_of_nodes() # Returns "825"
len(gen.__next__()) # Returns "3" - Python says next subsequent component has 3 nodes in it
len(gen.__next__()) # Returns "4" - Can run this multiple times until we run out of components
# len, when applied to a graph object, returns no. of nodes in that object
len(G1) # Returns "843"
G1.number_of_nodes() # Returns "843"
# max function can take in a generator as an input
G1_LCC = max((G1.subgraph(c) for c in nx.connected_components(G1)), key=len)
G2_LCC = max((G2.subgraph(c) for c in nx.connected_components(G2)), key=len)
len(G1_LCC) # Returns "825" - G1 contains 1 largest connected component that has 825 nodes in it
len(G2_LCC) # Returns "810" - G2 contains 1 largest connected component that has 810 nodes in it
len(G1_LCC) / len(G1) # Returns "0.9786476868327402" - Largest connect component is 98% of the graph
len(G2_LCC) / len(G2) # Returns "0.9236031927023945" - Largest connect component is 92% of the graph

# Let's visualise these components:
# Village 1:
plt.style.use("bmh")
plt.figure()
nx.draw(G1_LCC, edge_color="gray", node_size=20)
plt.savefig("village1.png")
# Village 2:
plt.style.use("bmh")
plt.figure()
nx.draw(G2_LCC, node_color=u'#A60628', edge_color="gray", node_size=20)
plt.savefig("village2.png")

######################################################
# 4.3.7 FINDING THE LARGEST CONNECTED COMPONENT - Quiz
######################################################
# Question 1: For an iterator object X, what does X.__next__() do?
# Solution 1: Returns the next value in X, if it exists

# Question 2: For a given network G, what does len(G) return?
# Solution 2: The number of nodes

# Question 3: Graphs G1 and G2 are defined as in Video 4.3.7. Which graph contains the largest connected component?
# Solution 3: G1

# Question 4: Which graph contains the greatest fraction of its nodes in its largest connected component?
# Solution 4: G1