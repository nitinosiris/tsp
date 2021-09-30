from Import import *

def kruskalAlgo(inp_graph):
    # stores the edges present in MST
    MST = []
    index = 0
    cost = 0
    nodes = inp_graph.number_of_nodes()
    # temp graph
    graph = nx.Graph()
    # sort edges by increasing weight
    sorted_graph = sorted(inp_graph.edges(data=True), key=lambda item: item[2]['weight'])
    # MST contains exactly `V-1` edges
    i = 0
    for edgelist in sorted_graph:
        # consider the next edge with minimum weight from the graph
        (src, dest, weight) = edgelist
        weight = weight.get('weight')
        index = index + 1
        # add edge
        graph.add_edge(src, dest, weight=weight)
        # check for cycle
        lst = nx.cycle_basis(graph.to_undirected())
        if len(lst) == 0:
            # consider the wt if no cycle
            cost = cost + weight
        else:
            # discard the edge
            e = (src, dest, {"weight" : weight})
            graph.remove_edge(*e[:2])
    cost = 0
    for s,d,wt in graph.edges(data="weight"):
        cost = cost + wt
    # print(cost)
    return graph, cost



#works
def get_g_n(inp_graph, src, dest, parent_g_n):
    e = (src, dest)
    if inp_graph.has_edge(*e):
        return inp_graph[src][dest].get('weight') + parent_g_n
    else:
        return -1



#works
def get_h_n_and_mst(inp_graph):
    graph, cost = kruskalAlgo(inp_graph)
    # print("Cost of MST " + str(cost))
    # print_graph(graph,0)
    return cost



#works
def remove_list_of_nodes_from_graph(src, inp_graph, lst):
    for i in lst:
        if int(i) != src:
            if int(i) in inp_graph:
                inp_graph.remove_node(int(i))
    return inp_graph



#works
def check_for_exactly_once_visited(input_graph ,visited):
    lst = list(input_graph)
    for i in lst:
        if i not in visited:
            return False
    return True