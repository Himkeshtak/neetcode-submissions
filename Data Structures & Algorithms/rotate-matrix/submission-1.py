class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # first take the reverse veritcally ( Sabse niche ki row ko sabse upar and sabse upar ki row at the bottom most), then take the transpose
        # there sxist the direct function to perform the reverse operations of the 2-D matrixc
        matrix.reverse()

        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]