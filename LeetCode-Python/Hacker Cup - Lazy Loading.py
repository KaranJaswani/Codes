# Wilson works for a moving company. His primary duty is to load household items into a moving truck. Wilson has a bag that he uses to move these items. He puts a bunch of items in the bag, moves them to the truck, and then drops the items off.
#
# Wilson has a bit of a reputation as a lazy worker. Julie is Wilson's supervisor, and she's keen to make sure that he doesn't slack off. She wants Wilson to carry at least 50 pounds of items in his bag every time he goes to the truck.
#
# Luckily for Wilson, his bag is opaque. When he carries a bagful of items, Julie can tell how many items are in the bag (based on the height of the stack in the bag), and she can tell the weight of the top item. She can't, however, tell how much the other items in the bag weigh. She assumes that every item in the bag weighs at least as much as this top item, because surely Wilson, as lazy as he is, would at least not be so dense as to put heavier items on top of lighter ones. Alas, Julie is woefully ignorant of the extent of Wilson's lack of dedication to his duty, and this assumption is frequently incorrect.
#
# Today there are N items to be moved, and Wilson, paid by the hour as he is, wants to maximize the number of trips he makes to move all of them to the truck. What is the maximum number of trips Wilson can make without getting berated by Julie?
#
# Note that Julie is not aware of what items are to be moved today, and she is not keeping track of what Wilson has already moved when she examines each bag of items. She simply assumes that each bagful contains a total weight of at least k * w where k is the number of items in the bag, and w is the weight of the top item.
#
# Input
# Input begins with an integer T, the number of days Wilson "works" at his job. For each day, there is first a line containing the integer N. Then there are N lines, the ith of which contains a single integer, the weight of the ith item, Wi.
#
# Output
# For the ith day, print a line containing "Case #i: " followed by the maximum number of trips Wilson can take that day.
#
# Constraints
# On every day, it is guaranteed that the total weight of all of the items is at least 50 pounds.
#
# Explanation of Sample
# In the first case, Wilson can make two trips by stacking a 30-pound item on top of a 1-pound item, making the bag appear to contain 60 pounds.
#
# In the second case, Wilson needs to put all the items in the bag at once and can only make one trip.
#
# In the third case, one possible solution is to put the items with odd weight in the bag for the first trip, and then the items with even weight in the bag for the second trip, making sure to put the heaviest item on top.
#
# Example input
# 5
# 4
# 30
# 30
# 1
# 1
# 3
# 20
# 20
# 20
# 11
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 6
# 9
# 19
# 29
# 39
# 49
# 59
# 10
# 32
# 56
# 76
# 8
# 44
# 60
# 47
# 85
# 71
# 91
# Example output
# Case #1: 2
# Case #2: 1
# Case #3: 2
# Case #4: 3
# Case #5: 8

import math

def driverFunction():
    lines = []
    with open('/Users/karanjaswani/Desktop/lazy_loading.txt') as f:
        for line in f:
            lines.append(int(line))
    f.close()

    days = int(lines[0])
    k = 1
    f = open('/Users/karanjaswani/Desktop/lazy_loading_output.txt', "w")
    for i in xrange(0, days):
        count = LazyLoading(lines[k + 1 : k + lines[k] + 1])
        k = k + lines[k] + 1
        f.write('Case #%d: %d\n' % (i + 1, count))

    f.close()


def LazyLoading(lst):
    """
    :param lst: List[int]
    :return: int
    """
    lst.sort(reverse=True)
    i = 0
    j = len(lst)
    count = 0

    while(i < j):
        item = lst[i]
        itemsNeeded = int(math.ceil(50.0 / item))
        if itemsNeeded > 0: itemsNeeded -= 1
        if j - i > itemsNeeded:
            count += 1
        else:
            break
        i = i + 1
        j = j - itemsNeeded

    return count

driverFunction()


#!/usr/bin/env python
#global
MIN_WEIGHT = 50

def trips(weights):
    t = 0
    weights.sort()
    i = 0
    j = len(weights)-1
    while i <= j:
        count = 0
        if weights[j] < MIN_WEIGHT:
            count = MIN_WEIGHT / weights[j]
            if MIN_WEIGHT % weights[j] == 0:
                count -= 1
            if i + count > j:
                break # we are done
        j -= 1
        i += count
        t += 1
    return t

def main():
    f = open('/Users/karanjaswani/Desktop/lazy_loading.txt', 'r')
    o = open('/Users/karanjaswani/Desktop/lazy_loading_output_jai.txt', 'w')
    for i in range(0, int(f.readline())):
        weights = []
        for j in range(0, int(f.readline())):
            weights.append(int(f.readline()))
        o.write("Case #%d: %s\n"%(i+1,trips(weights)))
        #print "Case #%d: %s"%(i+1,trips(weights))
    f.close()
    o.close()

# Start program
if __name__ == "__main__":
   main()






