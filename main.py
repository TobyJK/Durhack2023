def printBoard(board):
    for i in range(7, -1, -1):
        print(board[i])

class piece:
    def __init__(self, colour):
        self.colour = colour
        self.moved = False
    
class pawn(piece):
    def __init__(self, colour):
        super().__init__(colour)
    
    def listMoves(self):
        for i in range(8):
            if self in board[i]:
                position = [i, board[i].index(self)]
                break

        positions = []
        if self.colour == 0:
            if not self.moved and position[0] == 1:
                positions.append([position[0]+2, position[1]])
            positions.append([position[0]+1, position[1]])
            
            try:
                if board[position[0]+1][position[1]+1].colour == 1:
                    positions.append([position[0]+1, position[1]+1])
            except:
                pass
            try:
                if board[position[0]+1][position[1]-1].colour == 1:
                    position.append([position[0]+1, position[1]-1])
            except:
                pass
        else:
            if not self.moved:
                positions.append([position[0]-2, position[1]])
            positions.append([position[0]-1, position[1]])
            
            try:
                if board[position[0]-1][position[1]+1].colour == 0:
                    positions.append([position[0]-1, position[1]+1])
            except:
                pass
            try:
                if board[position[0]-1][position[1]-1].colour == 0:
                    position.append([position[0]-1, position[1]-1])
            except:
                pass
        return positions

class rook(piece):
    def __init__(self, colour):
        super().__init__(colour)

class knight(piece):
    def __init__(self, colour):
        super().__init__(colour)

class bishop(piece):
    def __init__(self, colour):
        super().__init__(colour)

class queen(piece):
    def __init__(self, colour):
        super().__init__(colour)

class king(piece):
    def __init__(self, colour):
        super().__init__(colour)

board = [[rook(0), knight(0), bishop(0), queen(0), king(0), bishop(0), knight(0), rook(0)], [pawn(0), pawn(0), pawn(0), pawn(0), pawn(0), pawn(0), pawn(0), pawn(0)], [None, None, None, pawn(1), None, None, None, None], [None, None, None, None, None, None, None, None]]

print(board[1][2].listMoves())