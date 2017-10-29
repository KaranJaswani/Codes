# Some progress bars fill you with anticipation. Some are finished before you know it and make you wonder why there was a progress bar at all.
#
# Some progress bars progress at a pleasant, steady rate. Some are chaotic, lurching forward and then pausing for long periods. Some seem to slow down as they go, never quite reaching 100%.
#
# Some progress bars are in fact not bars at all, but circles.
#
# On your screen is a progress pie, a sort of progress bar that shows its progress as a sector of a circle. Envision your screen as a square on the plane with its bottom-left corner at (0, 0), and its upper-right corner at (100, 100). Every point on the screen is either white or black. Initially, the progress is 0%, and all points on the screen are white. When the progress percentage, P, is greater than 0%, a sector of angle (P% * 360) degrees is colored black, anchored by the line segment from the center of the square to the center of the top side, and proceeding clockwise.
#
#
# While you wait for the progress pie to fill in, you find yourself thinking about whether certain points would be white or black at different amounts of progress.
#
# Input
# Input begins with an integer T, the number of points you're curious about. For each point, there is a line containing three space-separated integers, P, the amount of progress as a percentage, and X and Y, the coordinates of the point.
#
# Output
# For the ith point, print a line containing "Case #i: " followed by the color of the point, either "black" or "white".
#
# Constraints
# Whenever a point (X, Y) is queried, it's guaranteed that all points within a distance of 10-6 of (X, Y) are the same color as (X, Y).
#
# Explanation of Sample
# In the first case all of the points are white, so the point at (55, 55) is of course white.
#
# In the second case, (55, 55) is close to the filled-in sector of the circle, but it's still white.
#
# In the third case, the filled-in sector of the circle now covers (55, 55), coloring it black.
import math

def driverFunction():
    lines = []
    with open('/Users/karanjaswani/Desktop/progress_pie.txt') as f:
        lines = f.readlines()
    f.close()

    input = int(lines[0])

    f = open('/Users/karanjaswani/Desktop/progress_pie_output.txt', "w")
    for i in xrange(1, input + 1):
        lst = lines[i].split()
        result = progressPie(int(lst[0]), int(lst[1]), int(lst[2]))
        f.write('Case #%d: %s\n' % (i, result))

    f.close()


def progressPie(percent, xCoord, yCoord):
    yCoord -= 50
    xCoord -= 50
    if (xCoord*xCoord) + (yCoord*yCoord) > 50*50:
        return "white"

    percentAngle = percent * 3.6

    pointAngleFromXLine = math.degrees(math.atan(yCoord * 1.0 / xCoord * 1.0))
    if xCoord<0 and yCoord < 0:
        pointAngleFromXLine = 180 + pointAngleFromXLine
    elif yCoord < 0:
        pointAngleFromXLine += 360
    elif xCoord < 0:
        pointAngleFromXLine = 180 + pointAngleFromXLine


    if (xCoord >= 0 and yCoord >= 0) :
        if percentAngle + pointAngleFromXLine >= 90:
            return "black"
        else:
            return "white"
    else:
        if percentAngle + pointAngleFromXLine > 450:
            return "black"
        else:
            return "white"


driverFunction()


#!/usr/bin/env python
import math
#global

RADIUS_SQ = 2500
BLACK = 'black'
WHITE = 'white'

def incirle(x,y):
    return RADIUS_SQ >= (x*x + y*y)

def progress_theta(p):
    return p*3.6

def theta_xy(x,y):
    if x == 0:
        if y >= 0:
            return 0
        else:
            return 180
    if y == 0:
        if x > 0:
            return  90
        else:
            return 270
    theta = math.degrees(math.atan(abs(x)*1.0/abs(y)))
    if x > 0 and y < 0:
        theta = 180 - theta
    elif x < 0 and y < 0:
        theta += 180
    elif x < 0 and y > 0:
        theta = 360 - theta
    return theta


def black_or_white(p, x, y):
    #shift the origin to 50,50
    x -= 50
    y -= 50
    if not incirle(x,y) or theta_xy(x,y) > progress_theta(p):
        return WHITE
    return BLACK

def main():
    f = open('/Users/karanjaswani/Desktop/progress_pie.txt', 'r')
    o = open('/Users/karanjaswani/Desktop/progress_pie_output_jai.txt', 'w')
    for i in range(0, int(f.readline())):
        arr = f.readline().split()
        assert len(arr) == 3
        p = int(arr[0])
        x = int(arr[1])
        y = int(arr[2])
        o.write("Case #%d: %s\n"%(i+1,black_or_white(p,x,y)))
        print "case #%d: %s"%(i+1,black_or_white(p,x,y))
    f.close()
    o.close()


# Start program
if __name__ == "__main__":
   main()










