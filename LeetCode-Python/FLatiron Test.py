def solution(T):
    lst = []
    result = []
    capital = 0

    for i in xrange(0, len(T)):
        if T[i] == i:
            capital = i
        lst.append([])
        result.append(0)

    for i in xrange(0, len(T)):
        if T[i] != i:
            lst[T[i]].append(i)

    k = 0
    queue = [capital]
    currentLevel = 1
    nextLevel = 0
    count = 0
    while len(queue) != 0:
        node = queue.pop(0)
        currentLevel -= 1
        count += 1

        for i in lst[node]:
            queue.append(i)
            nextLevel += 1

        if currentLevel == 0:
            currentLevel = nextLevel
            nextLevel = 0
            result[k] = count
            k += 1
            count = 0

    result.pop(0)

    return result


solution([])



# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(N, S):
    return count_families(parse_seats(S, N))

def getIndex(c):
    if c.upper() == 'J':
        return 8
    if c.upper() == 'K':
        return 9
    else:
        return ord(c.upper()) - ord('A')


def parse_seats(taken, rows):
    seat_plan = [[0 for x in range(10)] for y in range(rows)]
    for seat in taken.split():
        #seat is 40A or 2B or 15J etc..
        col = getIndex(seat[-1])
        row = int(seat[:-1])
        seat_plan[row-1][col] = 1;
    return seat_plan;

def count_families(seat_plan):
    count = 0;
    for row in seat_plan:
        if row[0] == 0 and row[1] == 0 and row[2] == 0 :
            count += 1
        if row[3] == 0 and row[4] == 0 and row[5] == 0 :
            count += 1
        elif row[4] == 0 and row[5] == 0 and row[6] == 0 :
            count += 1
        if row[7] == 0 and row[8] == 0 and row[9] == 0 :
            count += 1
    return count

solution(1,'1a')


