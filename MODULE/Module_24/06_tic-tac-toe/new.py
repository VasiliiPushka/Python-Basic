class Cell:
    def __init__(self, number):
        self.number = number  # Номер клетки (1-9)
        self.is_empty = True   # Занята ли клетка
        self.symbol = " "      # Какой символ в клетке (X, O или пусто)

    def occupy(self, symbol):
        """Занимает клетку символом X или O."""
        if self.is_empty:
            self.symbol = symbol
            self.is_empty = False
            return True  # Ход успешен
        return False  # Клетка уже занята

    def __str__(self):
        """Возвращает символ в клетке для отображения."""
        return self.symbol


class Board:
    def __init__(self):
        # Создаём 9 клеток с номерами от 1 до 9
        self.cells = [Cell(i) for i in range(1, 10)]  # cells[0] = Cell(1), cells[1] = Cell(2) и т. д.

    def display(self):
        """Отображает поле в консоли."""
        for i in range(0, 9, 3):  # Выводим по 3 клетки в строке
            print(f"{self.cells[i]} | {self.cells[i + 1]} | {self.cells[i + 2]}")
            if i < 6:
                print("---------")

    def is_winner(self, symbol):
        """Проверяет, есть ли выигрышная комбинация для symbol (X или O)."""
        # Все возможные выигрышные комбинации (индексы клеток)
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Горизонтали
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Вертикали
            [0, 4, 8], [2, 4, 6]  # Диагонали
        ]
        for combo in win_combinations:
            if all(self.cells[i].symbol == symbol for i in combo):
                return True
        return False

    def is_draw(self):
        """Проверяет, наступила ли ничья (все клетки заняты)."""
        return all(not cell.is_empty for cell in self.cells)

    def make_move(self, cell_number, symbol):
        """Занимает клетку с номером cell_number символом symbol."""
        if 1 <= cell_number <= 9:
            cell = self.cells[cell_number - 1]  # Нумерация с 1 для пользователя
            return cell.occupy(symbol)
        return False


class Player:
    def __init__(self, name, symbol):
        self.name = name  # Имя игрока
        self.symbol = symbol  # X или O

    def make_move(self, board):
        """Запрашивает у игрока номер клетки и делает ход."""
        while True:
            try:
                cell_num = int(input(f"{self.name}, введите номер клетки (1-9): "))
                if 1 <= cell_num <= 9:
                    if board.make_move(cell_num, self.symbol):
                        break
                    else:
                        print("Клетка уже занята!")
                else:
                    print("Номер должен быть от 1 до 9!")
            except ValueError:
                print("Введите число!")


def play_game():
    # Создаём поле и игроков
    board = Board()
    player1 = Player("Игрок 1", "X")
    player2 = Player("Игрок 2", "O")
    current_player = player1

    print("Добро пожаловать в Крестики-нолики!")
    print("Номера клеток:")
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9")
    print("Начинаем игру!\n")

    while True:
        board.display()
        current_player.make_move(board)

        # Проверяем победу
        if board.is_winner(current_player.symbol):
            board.display()
            print(f"{current_player.name} победил!")
            break

        # Проверяем ничью
        if board.is_draw():
            board.display()
            print("Ничья!")
            break

        # Меняем игрока
        current_player = player2 if current_player == player1 else player1


# Запускаем игру
play_game()
