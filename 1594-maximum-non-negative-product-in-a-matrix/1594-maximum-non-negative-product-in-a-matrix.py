class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        m = len(grid)
        dp = [[[0,0] for _ in range(n)]for _ in range(m)]
        foundZero = False

        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == 0:
                   foundZero = True 

                if i == 0 and j == 0:
                    val = grid[0][0]
                    dp[i][j] = [val, val]             
                elif i == 0:
                    val = dp[i][j-1][0] * grid[i][j]
                    dp[i][j] = [val, val] 
                elif j == 0:
                    val = dp[i-1][j][0] * grid[i][j]
                    dp[i][j] = [val, val]
                else:
                    topOne = dp[i-1][j][0] * grid[i][j]
                    topTwo =  dp[i-1][j][1] * grid[i][j]

                    leftOne = dp[i][j-1][0] * grid[i][j]
                    leftTwo = dp[i][j-1][1] * grid[i][j]

                    minimum = min(topOne, topTwo, leftOne, leftTwo)
                    maximum = max(topOne, topTwo, leftOne, leftTwo)

                    dp[i][j][0] = minimum
                    dp[i][j][1] = maximum
        if foundZero and dp[m-1][n-1][1] == 0:
            return 0
        elif dp[m-1][n-1][1] < 1:
            return -1
        return dp[m-1][n-1][1] % (10**9 + 7)