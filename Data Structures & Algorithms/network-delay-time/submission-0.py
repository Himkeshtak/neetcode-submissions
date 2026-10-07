class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Djikstra

        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        ## Min-heap stores tuples of (distance, node
        minheap = [(0, k)]
        visit = set()
        t = 0
        while minheap:
            w1, n1 = heapq.heappop(minheap)
            ## Skip if already processed
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1

            
            # Explore neighbors
            for n2, w2 in edges[n1]:

                # Found a shorter path to neighbor
                if n2 not in visit:
                    heapq.heappush(minheap, (w1 + w2, n2))
        return t if len(visit) == n else -1