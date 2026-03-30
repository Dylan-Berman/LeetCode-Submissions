class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:

        for i in range(y, y + k):
            top = x
            bottom = x + k - 1
            while top < bottom:
                grid[top][i], grid[bottom][i] = grid[bottom][i], grid[top][i]
                bottom -= 1
                top +=1
        return grid

        