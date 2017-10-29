
#!/usr/bin/env python
import re

#globals
regex = re.compile('(\d+)d(\d+)(\+(\d+))?(\-(\d+))?')

def calc_probability(r, s):
    table = [[0.0 for x in range(r*s+1)] for y in range(r+1)]
    for i in range(1, s+1):
        table[1][i] = 1.0/s
    for i in range(2, r+1):
        for j in range(i, i*s+1):
            for k in range(1, s+1):
                if k >= j :
                    break
                table[i][j] += table[1][k]*table[i-1][j-k]
    return table

ptable = {4: calc_probability(20, 4),
          6: calc_probability(20, 6),
          8: calc_probability(20, 8),
          10: calc_probability(20, 10),
          12: calc_probability(20, 12),
          20: calc_probability(20, 20)}

def p_sum(r, s, t):
    p = 0.0
    while t <= r*s:
        print "s = %d r = %d t = %d" % (s, r, t)
        # print len(ptable)
        p += ptable[s][r][t]
        t += 1
    return format(p, '.6f')

def parse_string(spells, threshold):
    maxp = 0.0
    for spell in spells:
        m = regex.match(spell)
        if m is None:
            continue
        t = threshold
        if m.group(4) is not None:
            t -= int(m.group(4))
            if t < 0:
                print t
        elif m.group(6) is not None:
            t += int(m.group(6))
        x = int(m.group(1))
        y = int(m.group(2))
        val = p_sum(x, y, t)
        if val > maxp:
            maxp = val
    return maxp




def main():
    #print parse_string('2d4 1d8'.split(), 2)
    #print parse_string('10d6-10 1d6+1'.split(), 10)
    #print parse_string('1d4+4 2d4 3d4-4'.split(), 8)
    #print parse_string('10d4 5d8 2d20'.split(), 40)
    #print parse_string('1d10 1d10+1 1d10+2 1d10+3'.split(), 10)
    f = open('/Users/karanjaswani/Desktop/fighting_the_zombie.txt', 'r')
    o = open('/Users/karanjaswani/Desktop/fighting_the_zombie_output.txt', 'w')
    for i in range(0, int(f.readline())):
        arr = f.readline().split()
        h = int(arr[0])
        s = int(arr[1])
        spells = f.readline().split()
        assert len(spells) == s
        o.write("case #%d: %s\n"%(i+1,parse_string(spells, h)))
        #print "case #%d: %s"%(i+1,parse_string(spells, h))
    f.close()
    o.close()


main()

