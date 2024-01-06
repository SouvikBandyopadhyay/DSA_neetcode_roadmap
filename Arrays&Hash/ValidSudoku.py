class Solution:
    def checkbox(self, start, board):
        s = list()
        for i in range(3):
            for j in range(3):
                item = board[start[0]+i][start[1]+j]
                if item != ".":
                    s.append(item)
        return len(set(s)) == len(s)

    def isValidSudoku(self, board) -> bool:
        for i in range(9):
            seen = list()
            for j in range(9):
                item = board[i][j]
                if item != ".":
                    if item not in seen:
                        seen.append(item)
                    else:
                        return False
            seen = []
        for i in range(9):
            seen = list()
            for j in range(9):
                item = board[j][i]
                if item != ".":
                    if item not in seen:
                        seen.append(item)
                    else:
                        return False
            seen = []
        for i in range(3):
            for j in range(3):
                start = [i*3, j*3]
                print(start)
                if not self.checkbox(start, board):
                    return False
        return True
