class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        count  = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)
        
        min_h = list(count.keys())
        heapq.heapify(min_h)
        while min_h:
            first = min_h[0]
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != min_h[0]:
                        return False
                    heapq.heappop(min_h)
        return True
