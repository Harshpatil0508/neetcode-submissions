class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        boxes = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == '.':
                    continue
                
                if num in row[r]:
                    return False
                row[r].add(num)

                if num in col[c]:
                    return False
                col[c].add(num)

                box_index = (r//3,c//3)

                if num in boxes[box_index]:
                    return False
                boxes[box_index].add(num)
        return True
        