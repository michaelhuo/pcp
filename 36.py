import itertools
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board:
            return False
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i, j in itertools.product(range(9), range(9)):
            cell = board[i][j]
            if cell == '.':
                continue
            n = int(cell)
            if n in rows[i]:
                return False
            rows[i].add(n)
            # print(rows[i])

            if n in columns[j]:
                return False
            columns[j].add(n)
            # print(columns[j])

            idx = (i // 3) * 3 + j // 3
            if n in boxes[idx]:
                return False
            boxes[idx].add(n)
            
        return True
