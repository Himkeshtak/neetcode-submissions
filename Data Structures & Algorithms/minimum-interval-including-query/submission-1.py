import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        if not intervals:
            return []
        
        intervals.sort(key = lambda pair: pair[0])
        
        # Sort queries while keeping track of original indices: (query_val, original_index)
        sorted_queries = sorted((q, idx) for idx, q in enumerate(queries))
        
        output = [-1] * len(queries)
        min_heap = []  # Stores tuples: (interval_length, end_time)
        i = 0          # Pointer for intervals
        
        for j in range(len(sorted_queries)):
            query, orig_idx = sorted_queries[j]
            
            # Add all intervals starting <= current query to the heap
            while i < len(intervals) and intervals[i][0] <= query:
                heapq.heappush(min_heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
            
            # Remove intervals from heap that end < current query
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)
            
            # The top of the heap is the smallest interval containing the query
            if min_heap:
                output[orig_idx] = min_heap[0][0]
                
        return output
        