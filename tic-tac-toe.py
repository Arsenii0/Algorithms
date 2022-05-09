board = [3][3]

# TODO!


def init_default_board():
    for row in range(0, len(board)):
        for column in range(0, len(board[row])):
            board[row][column] = -1


def main():
    init_default_board()
    print(board)


if __name__ == "__main__":
    main()
