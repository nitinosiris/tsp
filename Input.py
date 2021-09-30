from Import import *

print("Enter the name of file on which you want to run this Alog : ")
inp = input()

G = nx.read_edgelist(inp, nodetype=int, data=(("weight", int),))
G = nx.Graph(G)


list(G.edges(data=True))
source = list(G.edges())
source, x = source[0]
print("-----------------------------------------------------------------")
print("source is " + str(source))


def print_graph(inp_graph, ct):
    pos = nx.spring_layout(inp_graph)
    nx.draw_networkx(inp_graph, pos)
    labels = nx.get_edge_attributes(inp_graph, 'weight')
    x = nx.draw_networkx_edge_labels(inp_graph, pos, edge_labels=labels)
    plt.show("filename" + str(ct) + ".png")


# Initialize
input_graph = copy.deepcopy(G)
no_of_nodes = input_graph.number_of_nodes()
pq = PriorityQueue()


print("No of nodes in graph " + str(input_graph.number_of_nodes()))
# print_graph(input_graph, 0)