# classes
# Game has Board and Player
# Board has pieces
# Player has name and piece

# Behaviour
# Game start end declare result
# Board init and reset
# Player can move piece

from collections import deque


class Piece:
    def __init__(self, symbol: str):
        self.symbol = symbol


class Player:
    def __init__(self, name: str, piece: Piece):
        self.name = name
        self.piece = piece


class Board:
    def __init__(self, size: int):
        self.size = size
        self.reset()

    def reset(self):
        self.board = [["-" for _ in range(self.size)] for _ in range(self.size)]
        self.turnCount = 0
        self.rowCount = {}
        self.colCount = {}
        self.diaCount = {}
        self.rDiaCount = {}

    def move(self, player: Player, row: int, col: int):
        if row > self.size - 1 or col > self.size - 1 or self.board[row][col] != "-":
            return False
        self.board[row][col] = player.piece.symbol
        # update rowCount
        currRowCount = self.rowCount.get(row, {})
        currRowCount[player.piece.symbol] = currRowCount.get(player.piece.symbol, 0) + 1
        self.rowCount[row] = currRowCount
        # update columnCount
        currColCount = self.colCount.get(col, {})
        currColCount[player.piece.symbol] = currColCount.get(player.piece.symbol, 0) + 1
        self.colCount[col] = currColCount
        # update dia, rDia count
        if row == col:
            self.diaCount[player.piece.symbol] = self.diaCount.get(player.piece.symbol, 0) + 1
        if self.size - row - 1 == col:
            self.rDiaCount[player.piece.symbol] = self.rDiaCount.get(player.piece.symbol, 0) + 1
        if self.checkWin(row, col, player):
            print(f"Player {player.name} won")
            raise Exception
        if self.turnCount == self.size * self.size:
            print("Tie")
            raise Exception
        return True

    def checkWin(self, row: int, col: int, player: Player):
        if (
            self.rowCount[row].get(player.piece.symbol, 0) == self.size
            or self.colCount[col].get(player.piece.symbol, 0) == self.size
            or self.diaCount.get(player.piece.symbol, 0) == self.size
            or self.rDiaCount.get(player.piece.symbol, 0) == self.size
        ):
            return True

    def print(self):
        for row in self.board:
            for col in row:
                print(col + " ", end="")
            print("")


class Game:
    def __init__(self, board: Board, players: list[Player]):
        self.board = board
        self.players = players
        self.turn = deque(players)
        self.over = False

    def play(self):
        while not self.over:
            currPlayer = self.turn.popleft()
            row, col = map(int, input(f"{currPlayer.name}, enter row and col: ").strip().split())
            try:
                if not self.board.move(currPlayer, row, col):
                    print("Invalid pos")
                    self.turn.appendleft(currPlayer)
                    continue
                self.turn.append(currPlayer)
            except:
                self.over = True
            finally:
                self.board.print()


x = Piece("x")
y = Piece("y")
z = Piece("z")
p1 = Player("dhruv", x)
p2 = Player("yash", y)
p3 = Player("me", z)
board = Board(4)
game = Game(board, [p1, p2, p3])
game.play()
