class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # people = sorted(people, key=lambda l: l[0])
        # result = []
        # while len(people) > 0:
        #     for i in xrange(0, len(people)):
        #         lst = people[i]
        #         if lst[1] == sum(l[0] >= lst[0] for l in result):
        #             result.append(lst)
        #             people.pop(i)
        #             break
        #
        # return result

        people = sorted(people, key=lambda l: (l[0], -l[1]), reverse=True)
        result = []
        for lst in people:
            result.insert(lst[1], lst)

        return result


obj = Solution()
obj.reconstructQueue([[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]])




