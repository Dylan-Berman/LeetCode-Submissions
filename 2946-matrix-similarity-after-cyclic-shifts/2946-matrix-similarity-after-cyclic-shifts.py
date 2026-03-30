class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        
        m = len(mat[0])
        n = len(mat)
        for i in range(n):
            for j in range(m):
                index = (j + k) % m
                if mat[i][index] != mat[i][j]:
                    return False
        return True