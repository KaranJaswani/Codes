dict = {"key1" : [[1,2],
                  [3,4],
                  [5,6]],
        "key2" : [[1,2],
                  [3,4],
                  [5,6]],
        "key3":  [[1, 2],
                  [3, 4],
                  [5,6]],
        "key4":  [[1, 2],
                  [3, 4],
                  [5,6]]
        }

d = {}

for key in dict.keys():
    d[key] = dict[key][0:1] + dict[key][2:]


print d


