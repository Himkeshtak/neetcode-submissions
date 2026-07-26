class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # use the Merge sort ot sort the list one and then pop from the stack and do the operation and then add

        stones.sort()

        for i in range(len(stones)):
            last, second_last = None, None
            if len(stones) == 1:
                return stones[0]
                
            last = stones.pop()
            second_last = stones.pop()

            if last == second_last:
                if not stones:
                    return 0
                    
                continue
            elif last > second_last:
                stones.append(last - second_last)
                stones.sort()

            elif last < second_last:
                stones.append(second_last - last)
                stones.sort()

            


