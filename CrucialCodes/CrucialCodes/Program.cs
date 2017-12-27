using System;

namespace CrucialCodes
{
	class MainClass
	{
		public static void Main(string[] args)
		{
			//Console.WriteLine("Hello World!");
			//BinarySearchTree newTree = new BinarySearchTree(2);
			//newTree.Insert(1);
			//newTree.Insert(3);
			//Console.WriteLine("InOrderTraversal : ");
			//newTree.InOrderTraversal(newTree);
			//Console.WriteLine("Pre-Order Traversal : ");
			//newTree.PreOrderTraversal(newTree);
			//Console.WriteLine("PostOrderTraversal : ");
			//newTree.PostOrderTraversal(newTree);


			//TreeNode node1 = new TreeNode(3);
			//TreeNode node2 = new TreeNode(9);
			//TreeNode node3 = new TreeNode(20);
			//TreeNode node4 = new TreeNode(15);
			//TreeNode node5 = new TreeNode(7);

			//node1.left = node2;
			//node1.right = node3;
			//node3.left = node4;
			//node3.right = node5;


			//node1.PrintLevelorder(node1);


			Graph g = new Graph(4);

			g.addEdge(0, 1);
			g.addEdge(0, 2);
			g.addEdge(1, 2);
			g.addEdge(2, 0);
			g.addEdge(2, 3);
			g.addEdge(3, 3);

			Console.Write("Following is Depth First Traversal \n");
			g.DFS(2);

			//	Console.Write("\n Following is Breadth First Traversal \n");
			//	g.BFS(2);


			//	Heap theHeap = new Heap(21);
			//	theHeap.Insert(40);
			//	theHeap.Insert(70);
			//	theHeap.Insert(20);
			//	theHeap.Insert(60);
			//	theHeap.Insert(50);
			//	theHeap.Insert(100);
			//	theHeap.Insert(82);
			//	theHeap.Insert(35);
			//	theHeap.Insert(90);
			//	theHeap.Insert(10);
			//	theHeap.DisplayHeap();

			//	Console.WriteLine("Inserting a new node with value 120");
			//	theHeap.Insert(120);
			//	theHeap.DisplayHeap();

			//	Console.WriteLine("Removing max element");
			//	theHeap.Remove();
			//	theHeap.DisplayHeap();

			//	Console.WriteLine("Changing root to 130");
			//	theHeap.HeapIncreaseDecreaseKey(0, 130);
			//	theHeap.DisplayHeap();

			//	Console.WriteLine("Changing root to 5");
			//	theHeap.HeapIncreaseDecreaseKey(0, 5);
			//	theHeap.DisplayHeap();
			//	Console.ReadLine();

			ListNode a = new ListNode(1);

			Solution s = new Solution();
			s.MergeKLists(new ListNode[] { null, a, });
		}
	}
}
