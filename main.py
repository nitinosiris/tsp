from Input import *
from Utility import *

def goal_test(src, visited):
    if src == visited[len(visited)-1] and len(visited)!=1:
        return True
    return False

def A_star(inp_graph, N, src):
    # state
    count = 1
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
        data = pq.get()
        f_n_parent, h_n_parent, g_n_parent, node, visited, parent = data
        count = max(pq.qsize(), count)
        # make node lst
        visited.append(node)

        if goal_test(src, visited):
            visited = [src] + visited
            print("-----------------------------------------------------------------")
            print("Path Followed is ")
            print(visited)
            return f_n_parent, count

        if check_for_exactly_once_visited(inp_graph , visited):
            print("-----------------------------------------------------------------")
            print("All nodes are visited exactly once")
            print(str(visited + [src]))

            x = visited[len(visited) -1]
            e = (x, src)

            if not inp_graph.has_edge(*e):
                print("No direct edges between " + str(x) + " and " + str(src))
                print("Prune above path :)")
                continue
            else:
                visited.remove(src)

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
            temp = copy.deepcopy(inp_graph)

            temp = remove_list_of_nodes_from_graph(src, temp, visited + [u])

            h_n = get_h_n_and_mst(temp)
            # edge wt + parent's gn
            GN = get_g_n(inp_graph, node, u, g_n_parent)
            
            if GN == -1:
                print("Direct edge doesn't exist for " + str(u) + " and " + str(node))
                break
            # push into heap
            pq.put((h_n + GN, h_n, GN, u, copy.deepcopy(visited),node))
            # count = count + 1
        
    if pq.qsize() == 0:
        # print("We haven't traversed all nodes and heap is empty")
        print("Solution does not exist")
        # print("Fail")
        ans = 0
    return ans, count



def Start_a_star():
    temp = copy.deepcopy(input_graph)
    # print_graph(input_graph, 0)
    path, count = A_star(input_graph, no_of_nodes, source)    
    print("FN = " + str(path))
    print("Max size of FringList during execution = " + str(count))
    print("-----------------------------------------------------------------")



Start_a_star()

