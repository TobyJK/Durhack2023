def printBoard(board):
    for i in range(7, -1, -1):
        print(board[i])

class piece:
    def __init__(self, colour):
        self.colour = colour
        self.moved = False
        self.letter = "X"
    def __repr__(self):
        return self.letter if self.colour == 0 else self.letter.lower()
    
class pawn(piece):
    def __init__(self, colour):
        super().__init__(colour)
        self.letter = "P"
    
    def listMoves(self):
        for i in range(8):
            if self in board[i]:
                position = [i, board[i].index(self)]
                break

        positions = []
        if self.colour == 0:
            if not board[position[0]+1][position[1]]:
                if not self.moved and position[0] == 1 and not board[position[0]+2][position[1]]:
                        positions.append([position[0]+2, position[1]])
                positions.append([position[0]+1, position[1]])
            
            try:
                if board[position[0]+1][position[1]+1].colour == 1:
                    positions.append([position[0]+1, position[1]+1])
            except:
                pass
            try:
                if board[position[0]+1][position[1]-1].colour == 1:
                    positions.append([position[0]+1, position[1]-1])
            except:
                pass
        else:
            if not board[position[0]-1][position[1]]:
                if not self.moved and position[0] == 6 and not board[position[0]-2][position[1]]:
                    positions.append([position[0]-2, position[1]])
                positions.append([position[0]-1, position[1]])
            
            try:
                if board[position[0]-1][position[1]+1].colour == 0:
                    positions.append([position[0]-1, position[1]+1])
            except:
                pass
            try:
                if board[position[0]-1][position[1]-1].colour == 0:
                    positions.append([position[0]-1, position[1]-1])
            except:
                pass
        return positions

class rook(piece):
    def __init__(self, colour):
        super().__init__(colour)
        self.letter = "R"

class knight(piece):
    def __init__(self, colour):
        super().__init__(colour)
        self.letter = "P"
    
    def listMoves(self):
        print()

class bishop(piece):
    def __init__(self, colour):
        super().__init__(colour)
        self.letter = "B"

class queen(piece):
    def __init__(self, colour):
        super().__init__(colour)
        self.letter = "Q"

class king(piece):
    def __init__(self, colour):
        super().__init__(colour)
        self.letter = "K"

board = [[rook(0), knight(0), bishop(0), queen(0), king(0), bishop(0), knight(0), rook(0)], 
         [pawn(0), pawn(0), pawn(0), pawn(0), pawn(0), pawn(0), pawn(0), pawn(0)], 
         [None, None, None, None, None, None, None, None], 
         [None, None, None, None, None, None, None, None], 
         [None, None, None, None, None, None, None, None], 
         [None, None, None, None, None, None, None, None], 
         [pawn(1), pawn(1), pawn(1), pawn(1), pawn(1), pawn(1), pawn(1), pawn(1)], 
         [rook(1), knight(1), bishop(1), queen(1), king(1), bishop(1), knight(1), rook(1)]]

printBoard(board)