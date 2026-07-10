class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #
        row, col = len(matrix) , len(matrix[0])
        l , r = 0 , row * col - 1
        while l <= r:

            mid = l + (r-l)//2
            i = mid // col # here divide by cols because the rows division doesnt make any sense
            j = mid % col
            if target > matrix[i][j]:
                l = mid + 1
            elif target < matrix[i][j]:
                r = mid - 1
            else:
                return True
        return False