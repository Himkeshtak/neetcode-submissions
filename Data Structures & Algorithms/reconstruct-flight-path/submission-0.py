class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # start with the JFK , go to JFK first element 
        # if the JFk has multiple elements then choose the 
        # lesser lexicographic first (dictionary order)
        # 
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)

        stack = ["JFK"]
        res = []

        while stack:
            curr = stack[-1]
            if not adj[curr]:
                res.append(stack.pop())
            else:
                stack.append(adj[curr].pop())
            
        return res[::-1]
