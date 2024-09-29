from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        # Create a DP array with an extra row and column filled with 0s
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        max_len = 0
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if matrix[i-1][j-1] == "1":
                    # we take min because if there is 0 in above, left and diagonal 
                    # since WE CAN'T form a triangle at dp[i][j]
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_len = max(max_len, dp[i][j])

        return max_len * max_len
    
# Time complexity: O(m x n)
# Space complexity: O(m x n) - because dp matrix

# Example usage:
if __name__ == "__main__":
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]

    solution = Solution()
    print(solution.maximalSquare(matrix))  # Should print 4
