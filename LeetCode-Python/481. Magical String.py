class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        str = "1"
        queue = ["22"]

        if n == 0:
            return 0
        elif n <=3:
            return 1
        else:
            n -= 3
            count = 1
            while n > 0:
                node  = queue.pop(0)
                str = str + node
                if node == "1":
                    if len(queue) == 0 or "2" in queue[-1]:
                        queue.append("1")
                        count += 1
                        n -= 1
                    else:
                        queue.append("2")
                        n -= 1

                elif node == "2":
                    if len(queue) == 0 or "1" in queue[-1]:
                        queue.append("22")
                        n -= 2
                    else:
                        queue.append("11")
                        if n >= 2:
                            count += 2
                        else:
                            count += 1
                        n -= 2

                elif node == "11":
                    if len(queue) == 0 or "1" in queue[-1]:
                        queue.append("2")
                        queue.append("1")
                        if n >= 2:
                            count += 1
                        n -= 2
                    else:
                        queue.append("1")
                        queue.append("2")
                        count += 1
                        n -= 2

                elif node == "22":
                    if len(queue) != 0:
                        if len(queue) == 0 or "1" in queue[-1]:
                            queue.append("22")
                            queue.append("11")
                            if n == 3:
                                count += 1
                            elif n >= 4:
                                count += 2

                            n -= 4
                        else:
                            queue.append("11")
                            queue.append("22")
                            if n == 1:
                                count += 1
                            else:
                                count += 2
                            n -= 4
                    else:
                        queue.append("11")
                        if n == 1:
                            count += 1
                        else:
                            count += 2
                        n -= 2

        return count





