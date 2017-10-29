class Heap(object):
    def __init__(self):
        self.arr = []

    def count(self):
        return len(self.arr)

    def isEmpty(self):
        return len(self.arr) == 0

    def PushElement(self, element):
        self.arr.append(element)
        self.HeapifyUp()

    def PopElement(self):
        element = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        self.HeapifyDown(0)
        return element

    def GetElement(self):
        return self.arr[0]

    def HeapifyUp(self):
        i = len(self.arr) - 1
        while self.GetParent(i) >= 0 and self.arr[i] <= self.arr[self.GetParent(i)]:
            temp = self.arr[i]
            self.arr[i] = self.arr[self.GetParent(i)]
            self.arr[self.GetParent(i)] = temp
            i = self.GetParent(i)

    def HeapifyDown(self, i):
        left = self.GetLeftChild(i)
        right = self.GetRightChild(i)
        max = i

        if left < self.count() and self.arr[left] < self.arr[i]:
            max = left

        if right < self.count() and self.arr[right] < self.arr[max]:
            max = right

        if max != i:
            temp = self.arr[max]
            self.arr[max] = self.arr[i]
            self.arr[i] = temp
            self.HeapifyDown(max)
        else:
            return

    def GetParent(self, i):
        return (i - 1) / 2

    def GetLeftChild(self, i):
        return 2 * i + 1

    def GetRightChild(self, i):
        return 2 * i + 2