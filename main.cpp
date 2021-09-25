
#include <bits/stdc++.h>
using namespace std;


typedef pair<int, int> pairs;

class Edge {
public:
	int src, dest, weight;
};

class Graph {
public:
	
	// V-> Number of vertices, E-> Number of edges
	int V, E;

	// graph is represented as an array of edges.
	// Since the graph is undirected, the edge
	// from src to dest is also edge from dest
	// to src. Both are counted as 1 edge here.
	int **mat;
};

// Creates a graph with V vertices and E edges
Graph* createGraph(int V)
{
	Graph* graph = new Graph;
	graph->V = V;

	graph->mat = new int* [V];
    for (int i = 0; i < V; i++) {
        graph->mat[i] = new int[V];
    }

	return graph;
}


// // Compare two edges according to their weights.
// // Used in qsort() for sorting an array of edges
// int myComp(const void* a, const void* b)
// {
// 	Edge* a1 = (Edge*)a;
// 	Edge* b1 = (Edge*)b;
// 	return a1->weight > b1->weight;
// }

// // The main function to construct MST using Kruskal's
// // algorithm
// void KruskalMST(Graph* graph)
// {
// 	int V = graph->V;
// 	Edge result[V]; // Tnis will store the resultant MST
// 	int e = 0; // An index variable, used for result[]
// 	int i = 0; // An index variable, used for sorted edges
// 	set<pairs> st;
// 	// Step 1: Sort all the edges in non-decreasing
// 	// order of their weight. If we are not allowed to
// 	// change the given graph, we can create a copy of
// 	// array of edges
// 	qsort(graph->edge, graph->E, sizeof(graph->edge[0]),
// 		myComp);

// 	// Number of edges to be taken is equal to V-1
// 	while (e < V - 1 && i < graph->E)
// 	{
// 		// Step 2: Pick the smallest edge. And increment
// 		// the index for next iteration
// 		Edge next_edge = graph->edge[i++];
// 		pairs x = make_pair(next_edge.src, next_edge.dest);
// 		if(st.find(x) == st.end())
// 		{
// 			result[e++] = next_edge;
// 			st.insert(x);
// 		}
// 		// Else discard the next_edge
// 	}

// 	// print the contents of result[] to display the
// 	// built MST
// 	cout << "Following are the edges in the constructed "
// 			"MST\n";
// 	int minimumCost = 0;
// 	for (i = 0; i < e; ++i)
// 	{
// 		cout << result[i].src << " -- " << result[i].dest
// 			<< " == " << result[i].weight << endl;
// 		minimumCost = minimumCost + result[i].weight;
// 	}
// 	// return;
// 	cout << "Minimum Cost Spanning Tree: " << minimumCost
// 		<< endl;
// }

// // Driver code
int main()
{
	int V = 2;
	Graph *g;
	int temp;
	int ct = 0;
	g->V = V;
	g = createGraph(V);
	for(int i=0; i<V; i++)
	{
		for(int j=0; j<V; j++)
		{
			cin >> temp;
			g->mat[i][j] = temp;
			if(temp != 0)
			{
				ct++;
			}
		}
	}
	g->E = ct;

	cout << g->V << " " << g->E;
	for(int i=0;i<g->V;i++)
	{
		for(int j=0;j<g->V;j++)
		{
			cout << g->mat[i][j] << " ";
		}
		cout << "\n";
	}

	return 0;
}

// This code is contributed by rathbhupendra
