using System;
using System.Collections.Generic;
namespace CrucialCodes
{

	public class Graph
	{
		private int vertices;   // No. of vertices

		// Array  of lists for Adjacency List Representation
		private List<int>[] adj;

		// Constructor
		public Graph(int incomingVertices)
		{
			vertices = incomingVertices;
			adj = new List<int>[incomingVertices];
			for (int i = 0; i < incomingVertices; ++i)
				adj[i] = new List<int>();
		}

		//Function to add an edge into the graph
		public void addEdge(int v, int w)
		{
			adj[v].Add(w);  // Add w to v's list.
		}

		// A function used by DFS
		void DFSUtil(int v, bool[] visited)
		{
			// Mark the current node as visited and print it
			visited[v] = true;
			Console.Write(v + " ");

			// Recur for all the vertices adjacent to this vertex
			foreach (var link in adj[v])
			{
				if (!visited[link])
					DFSUtil(link, visited);
			}
		}

		// The function to do DFS traversal. It uses recursive DFSUtil()
		public void DFS(int v = -1)
		{
			// Mark all the vertices as not visited(set as
			// false by default in java)
			bool[] visited = new bool[vertices];

			if (v == -1)
			{
				// Call the recursive helper function to print DFS traversal
				// starting from all vertices one by one
				for (int i = 0; i < vertices; ++i)
					if (visited[i] == false)
						DFSUtil(i, visited);
			}
			else
			{
				DFSUtil(v, visited);
			}

		}

		// prints BFS traversal from a given source s
		public void BFS(int s)
		{
			// Mark all the vertices as not visited(By default
			// set as false)
			bool[] visited = new bool[vertices];

			// Create a queue for BFS
			Queue<int> queue = new Queue<int>();

			// Mark the current node as visited and enqueue it
			visited[s] = true;
			queue.Enqueue(s);

			while (queue.Count != 0)
			{
				// Dequeue a vertex from queue and print it
				int lastNode = queue.Dequeue();
				Console.Write(lastNode + " ");

				// Get all adjacent vertices of the dequeued vertex s
				// If a adjacent has not been visited, then mark it
				// visited and enqueue it
				foreach (var item in adj[lastNode])
				{
					if (!visited[item])
					{
						visited[item] = true;
						queue.Enqueue(item);
					}
				}
			}
		}
	}
}
