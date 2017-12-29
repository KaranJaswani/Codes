class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        def helper(current, cost, dp):
            if current >= len(cost):
                return 0

            if current in dp:
                return dp[current]

            dp[current] = cost[current] + \
                min(helper(current + 1, cost, dp), helper(current + 2, cost, dp))
            return dp[current]

        dp = {}
        return min(helper(0, cost, dp), helper(1, cost, dp))
