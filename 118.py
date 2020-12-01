class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result =[[1],[1,1]]
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return result
        for i in range(2, numRows):
            row = [1]
            prev = result[i - 1]
            for j in range(i - 1):
                row.append(prev[j] + prev[j + 1])
            row.append(1)
            result.append(row)
        return result
