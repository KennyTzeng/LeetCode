class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        width = len(board[0])-1
        height = len(board)-1
        count = 0
        
        for y in range(height+1):
            for x in range(width+1):
                if board[y][x] == "X":
                    if (x < width and board[y][x+1] == "X") or (y < height and board[y+1][x] == "X"):
                        continue
                    elif (x == width and y < height and board[y+1][x] == ".") or (y == height and x < width and board[y][x+1] == ".") or (x == width and y == height) or (x < width and y < height and board[y][x+1] == "." and board[y+1][x] == "."):
                        count += 1

        return count
        