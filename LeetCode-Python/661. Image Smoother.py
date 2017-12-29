class Solution(object):
    def imageSmoother(self, M):
        arr = []
        
        N = [[0 for col in range(len(M[0]))] for row in range(len(M))]
        
        for i in xrange(0, len(M)):
            for j in xrange(0, len(M[0])):
                arr.append([0,0])
                if j - 1 >= 0:
                    arr.append([0, -1])
                if j + 1 < len(M[0]):
                    arr.append([0, 1])
                if i - 1 >= 0:
                    if j - 1 >= 0:
                        arr.append([-1,-1])
                    arr.append([-1, 0])
                    if j + 1 < len(M[0]):
                        arr.append([-1, 1])
                if i + 1 < len(M):
                    if j - 1 >= 0:
                        arr.append([1, -1])
                    arr.append([1, 0])
                    if j + 1 < len(M[0]):
                        arr.append([1,1])
                summe = 0
                for ark in arr:
                    summe += M[ark[0] + i][ark[1] + j]
                N[i][j] = int(math.floor(summe / len(arr)))
                arr = []
        return N