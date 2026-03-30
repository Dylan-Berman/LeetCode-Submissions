class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        w = 0
        while w < 4:
            for i in range(n):
                for j in range(i, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

            for i in range(n):
                mat[i].reverse()

            if mat == target:
                return True
            w += 1    
        return False