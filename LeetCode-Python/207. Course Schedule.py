class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        hash = {}
        for i in range(0, numCourses):
            hash[i] = []

        for i in range(0, len(prerequisites)):
            hash[prerequisites[i][0]].append(prerequisites[i][1])

        used = []
        visited = []
        queue = []
        for i in range(0, numCourses):
            if i not in visited:
                used.append(i)
                queue.append(i)
                if not self.helperCanFinish(hash,queue, visited, used):return False

        return True

    def helperCanFinish(self, hash, queue, visited, used):

        if len(queue) == 0:
            return True

        node = queue.pop(0)
        used.append(node)
        for i in hash[node]:
            if i not in visited:
                if i in used: return False
                if i not in queue:
                    queue.append(i)

        if not self.helperCanFinish(hash, queue, visited, used): return False
        visited.append(node)
        return True



obj = Solution()
obj.canFinish(4, [[0,2], [0,3], [1,2], [2,3]])
