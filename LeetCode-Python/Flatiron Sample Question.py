# Given a string representing taken seats on a plane and a number N representing the rows on a plane,
# return the amount of seating arrangements for a family of 3. Seating between isles is not a possible arrangement.
# The seating columns are as follows: ABC | DEFG| HJK

def seatingArrangement(str, N):
    """
    :param str: string with seating arrangement
    :param N: Number of rows
    :return: Number of arrangement for family of 3
    """



# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(N):
    # write your code in Python 2.7
    count = 0
    result = 0

    while N != 0 and N & 1 == 0:
        N = N >> 1

    while N != 0:
        if N & 1 == 0:
            count += 1
            result = max(result, count)
        else:
            count = 0

        N = N >> 1

    return result

solution(14)

def solution(A, K):
    # write your code in Python 2.7

    start = 0
    x = 0
    i = 0
    firstTime = True

    while x < len(A):
        element = A[i]
        while firstTime or i != start:
            firstTime = False
            temp = A[(i + K) % len(A)]
            A[(i + K) % len(A)] = element
            element = temp
            i = (i + K) % len(A)
            x += 1
            if x == len(A):
                break
        start = start + 1
        firstTime = True
        i = start

    return A

solution( [-1, -2, -3, -4, -5, -6], 10)