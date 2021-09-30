from Input import *
from Utility import *

def A_star(inp_graph, N, src):
    # flag
    flag = 0
    # var
    popped = 0
    # ans
    ans = 0
    # state
    count = 0
    # GN
    GN = 0
    # ct = []
    visited = []
    # deepcopy for aug graph
    temp = copy.deepcopy(inp_graph)

    h_n = get_h_n_and_mst(temp)
    # h_n = 0
    pq.put((h_n + GN, h_n, GN, src, copy.deepcopy(visited), src))
    # std bfs jaisa
    while pq.qsize() != 0:
        count = max(pq.qsize(), count)
        data = pq.get()
        f_n_parent, h_n_parent, g_n_parent, node, visited, parent = data
        ans = f_n_parent
        popped = node
        # make node lst
        visited.append(node)
        # print("-----------------------------------------------------------------")
        if goal_test(inp_graph , visited):
            # count = len(list(heap))
            print("Goal test ran once " + str(visited + [src]))
            # print(visited[len(visited) -1])
            x = visited[len(visited) -1]
            e = (x, src)
            if not inp_graph.has_edge(*e):
                print("No direct edges between " + str(x) + " and " + str(src))
                print("Prune above path :)")
                continue
            else:
                ans += inp_graph[visited[len(visited)-1]][src].get('weight')
                return ans, count
        # get edges of current node
        edges = []
        for u, v, weight in inp_graph.edges.data("weight"):
            if weight is not None:
                if u == node and v not in visited:
                    edges.append(v)
                elif v == node and u not in visited:
                    edges.append(u)
        # push all those childs into heap
        for u in edges:
            # deepcopy for aug graph
            temp = copy.deepcopy(inp_graph)
            # create augmented graph
            temp = remove_list_of_nodes_from_graph(src, temp, visited + [u])
            # generate MST of augmented graph
            h_n = get_h_n_and_mst(temp)
            # edge wt + parent's gn
            GN = get_g_n(inp_graph, node, u, g_n_parent)
            
            if GN == -1:
                print("Direct edge doesn't exist for " + str(u) + " and " + str(node))
                break
            # push into heap
            pq.put((h_n + GN, h_n, GN, u, copy.deepcopy(visited),node))
        
    if pq.qsize() == 0:
        # print("We haven't traversed all nodes and heap is empty")
        print("Solution does not exist")
        print("Fail")
        ans = 0
    return ans, count



def Start_a_star():
    temp = copy.deepcopy(input_graph)
    # print_graph(input_graph, 0)
    path, count = A_star(input_graph, no_of_nodes, source)    
    print("FN = " + str(path))
    print("Max size of heap during runtime = " + str(count))



Start_a_star()

