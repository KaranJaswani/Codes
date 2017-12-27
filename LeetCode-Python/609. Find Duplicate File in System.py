class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        contentHash = {}
        for path in paths:
            elements = path.split(' ')
            path = elements[0]
            files = elements[1:]
            for file in files:
                fileInfo = file[:-1].split('(')
                fileName = fileInfo[0]
                contents = fileInfo[1]
                if contents in contentHash:
                    contentHash[contents].append(path + "/" + fileName)
                else:
                    contentHash[contents] = [path + "/" + fileName]

        res = [] 
        for key in contentHash:
            if len(contentHash[key]) > 1:
               res.append(contentHash[key])

        return res 

obj = Solution()
obj.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"])