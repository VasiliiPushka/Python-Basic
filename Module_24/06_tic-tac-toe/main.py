class Cell:
    def __init__(self, number, busy=False):
        self.number = number
        self.busy = busy
class Board:
    def __init__(self):
        self.board = [Cell(i) for i in range(1, 10)]

    def print_board(self):
        print("-" * 13)
        for i in range(3):
            print("|", self.board[0 + i * 3].number, "|",
                  self.board[1 + i * 3].number, "|",
                  self.board[2 + i * 3].number, "|")
            print("-" * 13)

    def check_win(self):
        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7),
                     (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for each in win_coord:
            if self.board[each[0]].number == self.board[
                each[1]].number == self.board[each[2]].number:
                if player_1.symbol == self.board[each[0]].number:
                    print(f'Победил {player_1.name} !')
                else:
                    print(f'Победил {player_2.name} !')
                return True
        return False

    def check_busy(self, number):
        if self.board[number - 1].busy:
            return True
        return False


class Player:
    def __init__(self, name, symbol, win=False):
        self.name = name
        self.symbol = symbol
        self.win = win

    def go_cell(self, number, Board):
        Board.board[number - 1].busy = True
        Board.board[number - 1].number = self.symbol


player_1 = Player('Игрок 1', 'X')
player_2 = Player('Игрок 2', 'O')
board = Board()
count = 0


def Game(player, board):
    number = int(input(f'Куда ходит, {player.name}? '))
    if board.check_busy(number):
        print('Клетка занята!')
        Game(player, board)
    else:
        player.go_cell(number, board)


while True:
    board.print_board()
    if count % 2 == 0:
        Game(player_1, board)
        if board.check_win():
            break
    else:
        Game(player_2, board)
        if board.check_win():
            break
    count += 1
    if count == 9:
        print("!!!Ничья!!!")
        break
board.print_board()