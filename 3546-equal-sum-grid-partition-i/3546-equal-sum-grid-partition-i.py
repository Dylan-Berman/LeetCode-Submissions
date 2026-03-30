class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        r = len(grid[0])
        c = len(grid)

        columns = []
        rows = []

        for i in range(c):
            rows.append(sum(grid[i]))
        for i in range(r):
            columns.append(sum(row[i] for row in grid))
        
        totalR = sum(rows)
        before = 0
        for i in rows:
            before += i
            after = totalR - before
            if before == after:
                return True
        
        totalC = sum(columns)
        before = 0
        for i in columns:
            before += i
            after = totalC - before
            if before == after:
                return True
        return False


        return False