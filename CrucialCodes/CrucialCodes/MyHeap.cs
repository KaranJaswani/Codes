using System;
using System.Collections.Generic;

namespace CrucialCodes
{
	public class ListNode
	{
		public int val;
		public ListNode next;
		public ListNode(int x) { val = x; }
	}

	public class MyHeap
	{
		private List<ListNode> elements = new List<ListNode>();

		public int GetSize()
		{
			return elements.Count;
		}

		public bool Any()
		{
			return elements.Count > 0;
		}

		public ListNode GetMin()
		{
			return this.elements.Count > 0 ? this.elements[0] : null;
		}

		public void Add(ListNode item)
		{
			elements.Add(item);
			this.HeapifyUp(elements.Count - 1);
		}

		public ListNode PopMin()
		{
			if (elements.Count > 0)
			{
				ListNode item = elements[0];
				elements[0] = elements[elements.Count - 1];
				elements.RemoveAt(elements.Count - 1);

				this.HeapifyDown(0);
				return item;
			}

			throw new InvalidOperationException("no element in heap");
		}

		private void HeapifyUp(int index)
		{
			var parent = this.GetParent(index);
			if (parent >= 0 && elements[index].val < elements[parent].val)
			{
				var temp = elements[index];
				elements[index] = elements[parent];
				elements[parent] = temp;

				this.HeapifyUp(parent);
			}
		}

		private void HeapifyDown(int index)
		{
			var smallest = index;

			var left = this.GetLeft(index);
			var right = this.GetRight(index);

			if (left < this.GetSize() && elements[left].val < elements[index].val)
			{
				smallest = left;
			}

			if (right < this.GetSize() && elements[right].val < elements[smallest].val)
			{
				smallest = right;
			}

			if (smallest != index)
			{
				var temp = elements[index];
				elements[index] = elements[smallest];
				elements[smallest] = temp;

				this.HeapifyDown(smallest);
			}

		}

		private int GetParent(int index)
		{
			if (index <= 0)
			{
				return -1;
			}

			return (index - 1) / 2;
		}

		private int GetLeft(int index)
		{
			return 2 * index + 1;
		}

		private int GetRight(int index)
		{
			return 2 * index + 2;
		}
	}

	public class Solution
	{
		public ListNode MergeKLists(ListNode[] lists)
		{
			var fakehead = new ListNode(-1);
			var start = fakehead;
			var heap = new MyHeap();
			ListNode tempHead = null;

			foreach (var list in lists)
			{
				if (list != null)
				{
					heap.Add(list);
				}
			}

			while (heap.Any())
			{
				tempHead = heap.PopMin();

				start.next = tempHead;
				start = start.next;

				if (tempHead.next != null)
				{
					heap.Add(tempHead.next);
				}
			}

			return fakehead.next;
		}
	}
}


