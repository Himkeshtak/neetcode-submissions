class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        rate = 0
        piles.sort()
        l ,r = 1 , piles[-1]
        ans_rate = r
        while l <= r:
            mid = l + (r-l)//2
            rate = mid
            t_taken = 0
            for p in piles:
                t_taken += math.ceil(float(p) / rate) 

            if h < t_taken: #agar time zyada lag rha to rate ko tez karo
                l = mid + 1
            
            else:
                ans_rate = rate
                r = mid - 1 # agar time bahut kam lag raha to rate badhao
            
        return ans_rate
            