using System;
using System.Collections.Generic;

namespace CrucialCodes
{
	class Node
	{
		private int nodeItem;

		public Node(int value)
		{
			nodeItem = value;
		}

		public int GetValue()
		{
			return nodeItem;
		}
		public void SetValue(int id)
		{
			nodeItem = id;
		}
	}

	class Heap
	{
		private Node[] heapArray;
		private int maxSize;
		private int currentSize;

		public Heap(int maxHeapSize)
		{
			maxSize = maxHeapSize;
			currentSize = 0;
			heapArray = new Node[maxSize];
		}

		public bool IsEmpty()
		{
			return currentSize == 0;
		}

		public bool Insert(int value)
		{
			if (currentSize == maxSize)
				return false;
			Node newNode = new Node(value);
			heapArray[currentSize] = newNode;
			CascadeUp(currentSize++);
			return true;
		}

		public void CascadeUp(int index)
		{
			int parent = (index - 1) / 2;
			Node bottom = heapArray[index];
			while (index > 0 && heapArray[parent].GetValue() < bottom.GetValue())
			{
				heapArray[index] = heapArray[parent];
				index = parent;
				parent = (parent - 1) / 2;
			}
			heapArray[index] = bottom;
		}

		public Node Remove() // Remove maximum value node
		{
			Node root = heapArray[0];
			heapArray[0] = heapArray[--currentSize];
			CascadeDown(0);
			return root;
		}

		public void CascadeDown(int index)
		{
			int largerChild;
			Node top = heapArray[index];
			while (index < currentSize / 2)
			{
				int leftChild = 2 * index + 1;
				int rightChild = leftChild + 1;
				if (rightChild < currentSize && heapArray[leftChild].GetValue() < heapArray[rightChild].GetValue())
					largerChild = rightChild;
				else
					largerChild = leftChild;
				if (top.GetValue() >= heapArray[largerChild].GetValue())
					break;
				heapArray[index] = heapArray[largerChild];
				index = largerChild;
			}
			heapArray[index] = top;
		}

		public bool HeapIncreaseDecreaseKey(int index, int newValue)
		{
			if (index < 0 || index >= currentSize)
				return false;
			int oldValue = heapArray[index].GetValue();
			heapArray[index].SetValue(newValue);
			if (oldValue < newValue)
				CascadeUp(index);
			else
				CascadeDown(index);
			return true;
		}

		public void DisplayHeap()
		{
			Console.WriteLine();
			Console.Write("Elements of the Heap Array are : ");
			for (int m = 0; m < currentSize; m++)
				if (heapArray[m] != null)
					Console.Write(heapArray[m].GetValue() + " ");
				else
					Console.Write("-- ");
			Console.WriteLine();
			int emptyLeaf = 32;
			int itemsPerRow = 1;
			int column = 0;
			int j = 0;
			String separator = "...............................";
			Console.WriteLine(separator + separator);
			while (currentSize > 0)
			{
				if (column == 0)
					for (int k = 0; k < emptyLeaf; k++)
						Console.Write(' ');
				Console.Write(heapArray[j].GetValue());

				if (++j == currentSize)
					break;
				if (++column == itemsPerRow)
				{
					emptyLeaf /= 2;
					itemsPerRow *= 2;
					column = 0;
					Console.WriteLine();
				}
				else
					for (int k = 0; k < emptyLeaf * 2 - 2; k++)
						Console.Write(' ');
			}
			Console.WriteLine("\n" + separator + separator);
		}


		public class ListNode
		{
			public int val;
			public ListNode next;
			public ListNode(int x) { val = x; }
		}

		public class HeapNode
		{
			public int val;
			public int list;

			public HeapNode(int value, int l)
			{
				val = value;
				list = l;
			}
		}

		HeapNode[] heap;

		public ListNode MergeKLists(ListNode[] lists)
		{
			heap = new HeapNode[lists.Length];
			ListNode result = null;
			ListNode iterator = null;

			for (int i = 0; i < lists.Length; i++)
			{
				if (lists[i] != null)
				{
					heap[i] = new HeapNode(lists[i].val, i);
					Heapify(i);
				}
			}

			if (heap[0] != null)
			{
				iterator = new ListNode(heap[0].val);
			}
			else
				return null;
			
			result = iterator;

			while (true)
			{
				lists[heap[0].list] = lists[heap[0].list].next;
				if (lists[heap[0].list] != null)
					heap[0] = new HeapNode(lists[heap[0].list].val, heap[0].list);
				else
				{
					heap[0] = heap[heap.Length - 1];
					heap[heap.Length - 1] = null;
				}

				if (heap.Length == 0)
					break;

				ReverseHeapify(0);

				iterator.next = new ListNode(heap[0].val);
				iterator = iterator.next;
			}

			return result;
		}

		public void Heapify(int index)
		{
			int parent = (index - 1) / 2;
			HeapNode bottom = heap[index];

			while (index > 0 && heap[parent].val > bottom.val)
			{
				heap[index] = heap[parent];
				index = parent;
				parent = (parent - 1) / 2;
			}

			heap[index] = bottom;
		}

		public void ReverseHeapify(int index)
		{
			int heapSize = heap.Length;
			int largerChild;
			HeapNode top = heap[index];
			while (index < heapSize / 2)
			{
				int leftChild = 2 * index + 1;
				int rightChild = leftChild + 1;

				if (rightChild < heapSize && heap[leftChild].val < heap[rightChild].val)
					largerChild = rightChild;
				else
					largerChild = leftChild;
				
				if (top.val <= heap[largerChild].val)
					break;
				
				heap[index] = heap[largerChild];
				index = largerChild;
			}

			heap[index] = top;
		}

	}
}
