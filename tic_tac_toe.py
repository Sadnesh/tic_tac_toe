# Tic-tac-toe game
"""
1.Has 9 four sided box 
2.each can have three value (none,cross,circle)
3.if three of either cross or circle comes consecutively in either direction ie vertical, horizontal or diagonal then one of them wins
4.if both of them doesn't manage to form three straights then its a draw
5.unlike connect 4 it doesn't support gravity feature
"""
from typing import List

grid_box = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
]
cha = ["O", "X"]
grid = """
    {:>2}|{:>2}|{:>2}|
  ----------------
    {:>2}|{:>2}|{:>2}|
  ----------------
    {:>2}|{:>2}|{:>2}|
"""


def display_grid(grid_box):
    tmp = []
    for i in grid_box:
        tmp += i
    print(grid.format(*tmp))


def winner(ch):
    print(f"AND the winner is {ch}")


def horizontal(grid_box):
    for a in range(0, 3):
        if (
            (grid_box[a][0])
            and (grid_box[a][0] == grid_box[a][1])
            and (grid_box[a][0] == grid_box[a][2])
        ):
            ch = grid_box[a][0]
            winner(ch)
            return True
    return False


def vertical(grid_box):
    for a in range(0, 3):
        if (
            (grid_box[0][a])
            and (grid_box[0][a] == grid_box[1][a])
            and (grid_box[0][a] == grid_box[2][a])
        ):
            ch = grid_box[0][a]
            winner(ch)
            return True
    return False


def diagonal(grid_box):
    sth = grid_box[0][0]
    if grid_box[0][0]:
        for a in range(1, 3):
            if grid_box[a][a] != sth:
                break
        else:
            ch = grid_box[0][0]
            winner(ch)
            return True
        return False
    if (grid_box[0][2] == grid_box[1][1]) and grid_box[0][2] == grid_box[2][0]:
        ch = grid_box[0][2]
        winner(ch)
        return True
    return False


def state_of(grid_box):
    return horizontal(grid_box) or vertical(grid_box) or diagonal(grid_box)


def main():
    display_grid(grid_box)
    n = 0
    while n < 9:
        i = cha[n % 2]
        pos = input(f"Enter the position for player {i}: i.e 0 1\n").split(" ")
        if len(pos) != 2 and not pos[0].isdigit() and not pos[1].isdigit():
            continue
        per_row = int(pos[0])
        per_col = int(pos[1])
        if not grid_box[per_row][per_col]:  # == ""
            grid_box[per_row][per_col] = i
            n += 1
        else:
            print("Please enter a valid position!")
        display_grid(grid_box)
        if n >= 4:
            if state_of(grid_box):
                break
    else:
        print("It's a draw. GG")

    print("Thank you for playing!")


if __name__ == "__main__":
    main()
