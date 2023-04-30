# Objects:
# Game has Board, Player, Dice
# Board has Cell
# Cell has Snake/Ladder
# Snake/Ladder has start and end pos

# Behaviour:
# Game can start
# Dice can roll

from collections import deque
from random import randint


class Player:
    def __init__(self, name: str):
        self.name = name
        self.pos = 0


class Dice:
    def __init__(self, lBound=0, uBound=6, numDice=1):
        self.uBound = uBound
        self.lBound = lBound
        self.numDice = numDice

    def roll(self):
        cnt = 0
        for _ in range(self.numDice):
            cnt += randint(self.lBound, self.uBound)
        return cnt


class Jumpable:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


class Snake(Jumpable):
    def __init__(self, start: int, end: int):
        if end > start:
            raise Exception("Snake cannot have higher end than start")
        super().__init__(start, end)


class Ladder(Jumpable):
    def __init__(self, start: int, end: int):
        if end < start:
            raise Exception("Ladder cannot have lower end than start")
        super().__init__(start, end)


class Cell:
    def __init__(self, pos: int, **kwargs):
        self.pos = pos
        self.ladder = kwargs.get("snake", None)
        self.snake = kwargs.get("ladder", None)


class Board:
    def __init__(self, size: int, numSnakes: int, numLadders: int):
        self.size = size
        self.reset()
        self.prepare(numSnakes, numLadders)

    def reset(self):
        self.board = [Cell(i + j * self.size) for i in range(self.size) for j in range(self.size)]

    def prepare(self, numSnakes: int, numLadders: int):
        for _ in range(numLadders):
            start = randint(0, self.size * self.size - 1)
            end = randint(start, self.size * self.size - 1)
            snake = Ladder(start, end)
            self.board[start] = Cell(start, snake=snake)

        for _ in range(numSnakes):
            start = randint(0, self.size * self.size - 1)
            end = randint(0, start)
            ladder = Snake(start, end)
            self.board[start] = Cell(start, ladder=ladder)

    def print(self):
        for row in range(self.size):
            for col in range(self.size):
                print(f"{self.board[row + col*self.size]} ", end="")
            print("")


class Game:
    def __init__(self, board: Board, dice: Dice, players: list[Player]):
        self.board = board
        self.dice = dice
        self.players = players
        self.turn = deque(players)

    def start(self):
        done = False
        while not done:
            currPlayer = self.turn.popleft()
            diceRoll = self.dice.roll()
            newPos = currPlayer.pos + diceRoll
            while newPos >= self.board.size * self.board.size:
                diceRoll = self.dice.roll()
                newPos = currPlayer.pos + diceRoll
            print(f"{currPlayer.name} at {newPos}")
            if self.board.board[newPos].snake:
                snake = self.board.board[newPos].snake
                print(f"Snake ({snake.start} {snake.end}) at {newPos}")
                newPos = snake.end
                print(f"newpos is {snake.end}")
            elif self.board.board[newPos].ladder:
                ladder = self.board.board[newPos].ladder
                print(f"ladder ({ladder.start} {ladder.end}) at {newPos}")
                newPos = ladder.end
                print(f"newpos is {ladder.end}")
            currPlayer.pos = newPos
            if currPlayer.pos >= self.board.size * self.board.size - 1:
                print(f"{currPlayer.name} wins")
                done = True
            self.turn.append(currPlayer)


p1 = Player("dhruv")
p2 = Player("yash")
dice = Dice()
board = Board(10, 4, 4)
game = Game(board, dice, [p1, p2])
game.start()
