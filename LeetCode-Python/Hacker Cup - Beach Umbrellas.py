import math


def beachUmbrellas(N, M, lst):

    if N == 1:
        print M

    hash = {} # Window Size : Number of permutations
    totalSize = 2 * sum(lst)
    res = 0
    PlacesBetweenUmbrellas = N + 1
    factOfInnerElements = math.factorial(N - 2)

    for i in range(0, N):
        for j in range(i + 1, N):
            currentWindowSize = totalSize - lst[i] - lst[j] - 1
            if currentWindowSize <= M:
                if currentWindowSize not in hash:
                    slotsRemaining = M - currentWindowSize
                    hash[currentWindowSize] = factOfInnerElements * waysToPutSlotsInBetween(PlacesBetweenUmbrellas, slotsRemaining) * 2

                res += hash[currentWindowSize]

    print res % 1000000007


def waysToPutSlotsInBetween(places, slots):
    if slots <= 0:
        return 1

    res = 0
    for i in range(1, slots + 1):
        res += nCr(places, i) * nCr(i, slots - i)

    return res


def nCr(n, r):
    if n < r :
        return 1
    f = math.factorial
    return f(n) / f(r) / f(n - r)

beachUmbrellas(3,10, [1,2,3])
