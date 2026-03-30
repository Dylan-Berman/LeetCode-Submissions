class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even = [0] * 26
        odd = [0] * 26
        n = len(s1)

        for i in range(n):
            index1 = ord(s1[i]) - ord('a')
            index2 = ord(s2[i]) - ord('a')
            if i % 2:
                odd[index1] += 1
                odd[index2] -= 1
            else:
                even[index1] += 1                
                even[index2] -= 1
        return all(x == 0 for x in even) and all(x == 0 for x in odd)