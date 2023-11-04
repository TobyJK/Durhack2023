def printBoard(board):
    for i in range(7, -1, -1):
        print(board[i])

class piece:
    def __init__(self, colour):
        self.colour = colour
        self.moved = False
        self.letter = "X"
        self.points = 0

    def __repr__(self):
        return self.letter if self.colour == 0 else self.letter.lower()
    
class pawn(piece):
    def __init__(self, colour):
        super().__init__(colour)
        self.letter = "P"
        self.points = 1
    
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
        self.points = 5
    
    def listMoves(self):
        for i in range(8):
            if self in board[i]:
                position = [i, board[i].index(self)]
                break
        
        positions = []
        new = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for thing in new:
            current = [x for x in position]
            while True:
                current[0] += thing[0]
                current[1] += thing[1]
                if current[0] < 0 or current[1] < 0:
                    break
                try:
                    if not board[current[0]][current[1]]:
                        positions.append([x for x in current])
                    elif (self.colour == 0 and board[current[0]][current[1]].colour == 1) or (self.colour == 1 and board[current[0]][current[1]].colour == 0):
                        positions.append([x for x in current])
                        break
                    else:
                        break
                except IndexError:
                    break
        return positions

class knight(piece):
    def __init__(self, colour):
        super().__init__(colour)
        self.letter = "N"
        self.points = 3

    def listMoves(self):
        for i in range(8):
            if self in board[i]:
                position = [i, board[i].index(self)]
                break

        positions = []
        maybePositions = [[1, 2], [2, 1], [1, -2], [2, -1], [-1, 2], [-2, 1], [-1, -2], [-2, -1]]
        
        for new in maybePositions:
            if position[0]+new[0] >= 0 and position[1]+new[1] >= 0:
                try:
                    if not board[position[0]+new[0]][position[1]+new[1]]:
                        positions.append([position[0]+new[0], position[1]+new[1]])
                    else:
                        if (self.colour == 0 and board[position[0]+new[0]][position[1]+new[1]].colour == 1) or (self.colour == 1 and board[position[0]+new[0]][position[1]+new[1]].colour == 0):
                            positions.append([position[0]+new[0], position[1]+new[1]])
                except IndexError:
                    pass
        
        return positions

class bishop(piece):
    def __init__(self, colour):
        super().__init__(colour)
        self.letter = "B"
        self.points = 3

    def listMoves(self):
        for i in range(8):
            if self in board[i]:
                position = [i, board[i].index(self)]
                break
        
        positions = []
        new = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
        for thing in new:
            current = [x for x in position]
            while True:
                current[0] += thing[0]
                current[1] += thing[1]
                if current[0] < 0 or current[1] < 0:
                    break
                try:
                    if not board[current[0]][current[1]]:
                        positions.append([x for x in current])
                    elif (self.colour == 0 and board[current[0]][current[1]].colour == 1) or (self.colour == 1 and board[current[0]][current[1]].colour == 0):
                        positions.append([x for x in current])
                        break
                    else:
                        break
                except IndexError:
                    break
        return positions
    
class queen(piece):
    def __init__(self, colour):
        super().__init__(colour)
        self.letter = "Q"
        self.points = 9
    
    def listMoves(self):
        for i in range(8):
            if self in board[i]:
                position = [i, board[i].index(self)]
                break
        
        positions = []
        new = [[1, 1], [1, -1], [-1, -1], [-1, 1], [0, 1], [1, 0], [0, -1], [-1, 0]]
        for thing in new:
            current = [x for x in position]
            while True:
                current[0] += thing[0]
                current[1] += thing[1]
                if current[0] < 0 or current[1] < 0:
                    break
                try:
                    if not board[current[0]][current[1]]:
                        positions.append([x for x in current])
                    elif (self.colour == 0 and board[current[0]][current[1]].colour == 1) or (self.colour == 1 and board[current[0]][current[1]].colour == 0):
                        positions.append([x for x in current])
                        break
                    else:
                        break
                except IndexError:
                    break
        return positions

class king(piece):
    def __init__(self, colour):
        super().__init__(colour)
        self.letter = "K"
    
    def listMoves(self):
        for i in range(8):
            if self in board[i]:
                position = [i, board[i].index(self)]
                break

        positions = []
        maybePositions = [[0, 1], [1, 0], [1, 1], [0, -1], [-1, 0], [-1, -1], [1, -1], [-1, 1]]
        
        for new in maybePositions:
            if position[0]+new[0] >= 0 and position[1]+new[1] >= 0:
                try:
                    if not board[position[0]+new[0]][position[1]+new[1]]:
                        positions.append([position[0]+new[0], position[1]+new[1]])
                    else:
                        if (self.colour == 0 and board[position[0]+new[0]][position[1]+new[1]].colour == 1) or (self.colour == 1 and board[position[0]+new[0]][position[1]+new[1]].colour == 0):
                            positions.append([position[0]+new[0], position[1]+new[1]])
                except IndexError:
                    pass
        
        return positions

board = [[rook(0), knight(0), bishop(0), queen(0), king(0), bishop(0), knight(0), rook(0)], 
         [pawn(0), pawn(0), pawn(0), pawn(0), pawn(0), pawn(0), pawn(0), pawn(0)], 
         [None, None, None, None, None, None, None, None], 
         [None, None, None, None, queen(0), None, None, None], 
         [None, None, None, None, None, None, None, None], 
         [None, None, None, None, None, None, None, None], 
         [pawn(1), pawn(1), pawn(1), pawn(1), pawn(1), pawn(1), pawn(1), pawn(1)], 
         [rook(1), knight(1), bishop(1), queen(1), king(1), bishop(1), knight(1), rook(1)]]

printBoard(board)
print(board[3][4].listMoves())