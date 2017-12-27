using System;
using System.Collections.Generic;
namespace CrucialCodes
{
	public class BinarySearchTree
	{
		public int value { get; set; }

		public BinarySearchTree Left;
		public BinarySearchTree Right;
		public BinarySearchTree(int val)
		{
			value = val;
		}

		public void Insert(int val)
		{
			BinarySearchTree head = this;

			while (head != null)
			{
				if (val <= head.value)
				{
					if (head.Left != null)
					{
						head = head.Left;
					}
					else
					{
						head.Left = new BinarySearchTree(val);
						break;
					}
				}
				else
				{
					if (head.Right != null)
					{
						head = head.Right;
					}
					else
					{
						head.Right = new BinarySearchTree(val);
						break;
					}
				}
			}
		}

		public void PreOrderTraversal(BinarySearchTree head)
		{
			if (head == null)
				return;

			Print(head);
			PreOrderTraversal(head.Left);
			PreOrderTraversal(head.Right);
		}

		public void InOrderTraversal(BinarySearchTree head)
		{
			if (head == null)
				return;

			InOrderTraversal(head.Left);
			Print(head);
			InOrderTraversal(head.Right);
		}

		public void PostOrderTraversal(BinarySearchTree head)
		{
			if (head == null)
				return;

			PostOrderTraversal(head.Left);
			PostOrderTraversal(head.Right);
			Print(head);
		}

		public void Print(BinarySearchTree node)
		{
			Console.Write(node.value);
		}

		public int Size(BinarySearchTree head)
		{
			if (head == null)
				return 0;
			else
				return 1 + Size(head.Left) + Size(head.Right);
		}

		public int MaxDepth(BinarySearchTree head)
		{
			if (head == null)
				return 0;
			else
				return 1 + Math.Max(MaxDepth(head.Left), MaxDepth(head.Right));
		}

		public int minValue(BinarySearchTree head)
		{
			int result = 0;
			while (head != null)
			{
				result = head.value;
				head = head.Left;
			}

			return result;
		}

		public void doubleTree(BinarySearchTree head)
		{
			if (head == null)
				return;

			doubleTree(head.Left);
			doubleTree(head.Right);

			BinarySearchTree left = head.Left;
			head.Left = new BinarySearchTree(head.value);
			head.Left.Left = left;

		}

		//Given a tree and a sum, returns true if there is a path from the root 
		//down to a leaf, such that adding up all the values along the path
		//equals the given sum.
		bool hasPathSum(BinarySearchTree node, int sum)
		{
			if (node == null)
			{
				return (sum == 0);
			}
			else
			{
				int subSum = sum - node.value;
				return (hasPathSum(node.Left, subSum) || hasPathSum(node.Right, subSum));
			}
		}


		//Recursive printPaths helper -- given a node, and an array containing 
		//the path from the root node up to but not including this node, 
		//prints out all the root-leaf paths. 
		private void printPaths(BinarySearchTree node, int[] path, int pathLen)
		{
			if (node == null) return;

			// append this node to the path array 
			path[pathLen] = node.value;
			pathLen++;

			// it's a leaf, so print the path that led to here 
			if (node.Left == null && node.Right == null)
			{
				printArray(path);
			}
			else
			{
				printPaths(node.Left, path, pathLen);
				printPaths(node.Right, path, pathLen);
			}
		}

		void printArray(int[] path)
		{
			foreach (var item in path)
			{
				Console.Write(item + "\t");
			}
		}

		//My approach : read in preorder and then reverse the condition of BST to create a new tree
		// This is a recursive approach. Bottom Up
		public void Mirror(BinarySearchTree node)
		{
			if (node != null)
			{
				// do the sub-trees 
				Mirror(node.Left);
				Mirror(node.Right);

				// swap the left/right pointers 
				BinarySearchTree temp = node.Left;
				node.Left = node.Right;
				node.Right = temp;
			}
		}

		//For the key values 1...numKeys, how many structurally unique 
		//binary search trees are possible that store those keys?
		private bool isBST(BinarySearchTree head)
		{
			if (head == null)
			{
				return true;
			}
			else
			{
				if (head.Left != null && head.Left.value > head.value) return false;
				if (head.Right != null && head.Right.value < head.value) return false;

				return (isBST(head.Left) && isBST(head.Right));
			}
		}
	}

	public class TreeNode
	{
		public int val;
		public TreeNode left;
		public TreeNode right;
		public TreeNode(int x) { val = x; }

		public void PrintLevelorder(TreeNode root)
		{
			int height = Height(root);
			for (int d = 1; d <= height; d++)
				PrintGivenLevel(root, d);
		}

		public void PrintGivenLevel(TreeNode root, int level)
		{
			if (root == null) return;

			if (level == 1)
				Print(root.val);
			else if (level > 1)
			{
				PrintGivenLevel(root.left, level - 1);
				PrintGivenLevel(root.right, level - 1);
			}
		}

		public int Height(TreeNode head)
		{
			if (head == null)
				return 0;
			else
				return 1 + Math.Max(Height(head.left), Height(head.right));
		}

		void Print(int value)
		{
			Console.WriteLine(value + "\n");
		}
	}

	public class BinaryTreeIteratorTravels
	{
		public List<int> inorderTraversal(TreeNode root)
		{
			List<int> result = new List<int>();

			if (root == null)
				return result;

			Stack<TreeNode> stack = new Stack<TreeNode>();

			while (root != null || stack.Count != 0)
			{
				if (root != null)
				{
					stack.Push(root);
					root = root.left;
				}
				else
				{
					root = stack.Pop();
					result.Add(root.val);
					root = root.right;
				}
			}

			return result;
		}

		public List<int> preorderTraversal(TreeNode root)
		{
			List<int> result = new List<int>();

			if (root == null)
				return result;

			Stack<TreeNode> s = new Stack<TreeNode>();

			while (root != null || s.Count != 0)
			{
				if (root != null)
				{
					result.Add(root.val);
					s.Push(root);
					root = root.left;
				}
				else
				{
					root = s.Pop();
					root = root.right;
				}
			}

			return result;
		}

		public List<int> postorderTraversal(TreeNode root)
		{
			List<int> result = new List<int>();

			if (root == null)
				return result;
			
			TreeNode pre = null;
			Stack<TreeNode> stack = new Stack<TreeNode>();

			while (root != null || stack.Count != 0)
			{
				if (root != null)
				{
					stack.Push(root);
					root = root.left;
				}
				else 
				{
					root = stack.Peek();
					if (root.right == null || root.right == pre)
					{
						result.Add(root.val);
						stack.Pop();
						pre = root;
						root = null;
					}
					else
					{
						root = root.right;
					}
				}
			}

			return result;
		}
	}
}
