class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_b = ["(", "{", "["];
        stack = list()
        for i in range(len(s)):
            if s[i] in open_b:
                stack.append(s[i])
            else:
                if len(stack) == 0: return False
                popped = stack.pop()
                if (popped == "(" and s[i] != ")") or (popped == "{" and s[i] != "}") or (popped == "[" and s[i] != "]"):
                    return False

        return len(stack) == 0
