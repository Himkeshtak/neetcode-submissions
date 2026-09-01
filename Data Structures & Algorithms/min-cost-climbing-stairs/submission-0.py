class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # DP based bottom up approach in which we use memoization which is the 
        # the very optimized APPROACH to use the repeated subtrees of the decision trees so that the complexity of backtracking based approach O(2^n) comes down to the O(n).
        # The node iterates in the reverse manner for the explaination so the the limitations of the greedy approach is solved easily and the global min is found rather thatn the greedy local decision

        # here, the last elememnt of the cost is the no tthe last stair the last stair is after the last element of the cost array , its not clearly mentionned in the quesiton which makes it confusing but this the the assumption taken here
        cost.append(0)

        # we start from the second last elemen of the original cost array the last element is always zero and the 
        # for the reverse iteration we have -1` and we will iterate till we arrive tot the i = -1
        for i in range(len(cost)-3, -1, -1):

            cost[i] += min( cost[i+1], cost[i+2])
        return min(cost[0], cost[1])
