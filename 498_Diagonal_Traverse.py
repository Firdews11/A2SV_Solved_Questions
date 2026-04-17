class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        hash_map = {}
        m, n = len(mat), len(mat[0])
        ans = []
        for i in range(m):
            for j in range(n):
                if i+j not in hash_map:
                    hash_map[i+j]=[]
                hash_map[i+j].append(mat[i][j])

        for i in range(len(hash_map)):
            if i%2 == 0:
                ans.extend((hash_map[i])[::-1])

            else:
                ans.extend(hash_map[i])
        return ans
