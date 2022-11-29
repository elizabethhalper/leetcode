# 1337. The K Weakest Rows in a Matrix
# You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians).
# The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

# A row i is weaker than a row j if one of the following is true:

# The number of soldiers in row i is less than the number of soldiers in row j.
# Both rows have the same number of soldiers and i < j.
# Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        q = []
        ret = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    q.append((j,i)) # num soldiers more important, then row
                    break
                else:
                    if j == len(mat[i])-1:
                        q.append((j+1,i))
                    else:
                        continue

        if len(q) == 0:
            return [0]
        
        q = sorted(q, key=lambda x: (x[0], x[1]))
        for i in range(k):
            ret.append(q[i][1])
        
        return ret