#!/usr/bin/env python3


class TicTacToe:
    def __init__(self, n: int):
        self.board_size = n
        # Initialize counters for both player to keep count of their positions
        # on each row, col and diagonals(2).
        self.counters = [[0] * (2 * n + 2) for _ in range(2)]

    # identity the counter position to update.
    def _positions(self, r, c: int) -> list[int]:
        # we have to update row and col counters.
        pos = [r, self.board_size + c]

        # If the position is a diagonal or anti-diagonal and include those
        # counters as well.
        #
        # if r = c (diagonal).
        if r == c:
            pos.append(2 * self.board_size)

        # anti-diagonal
        if r + c == self.board_size - 1:
            pos.append(2 * self.board_size + 1)

        return pos

    def move(self, row: int, col: int, player: int) -> int:
        player_idx = player - 1

        # update the counters and if it is full (board_size), we have a winner.
        for i in self._positions(row, col):
            self.counters[player_idx][i] += 1
            if self.counters[player_idx][i] == self.board_size:
                return player
        return 0


if __name__ == "__main__":
    board = TicTacToe(3)
    print(f"{board.move(0, 0, 1)}")
    print(f"{board.move(0, 2, 2)}")
    print(f"{board.move(2, 2, 1)}")
    print(f"{board.move(1, 1, 2)}")
    print(f"{board.move(2, 0, 1)}")
    print(f"{board.move(1, 0, 2)}")
    print(f"{board.move(2, 2, 1)}")
    print(f"final counter: {board.counters}")

    print("**** Next ****")
    board = TicTacToe(3)
    print(f"{board.move(0, 0, 1)}")
    print(f"{board.move(1, 1, 2)}")
    print(f"{board.move(2, 2, 1)}")
    print(f"{board.move(0, 2, 2)}")
    print(f"{board.move(0, 1, 1)}")
    print(f"{board.move(2, 0, 2)}")
    print(f"final counter: {board.counters}")
