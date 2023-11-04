from tic_tac_toe import display_grid, state_of, grid_box, cha as char

positions = {
    "lt": [0, 0],
    "ct": [0, 1],
    "rt": [0, 2],
    "cl": [1, 0],
    "cc": [1, 1],
    "cr": [1, 2],
    "bl": [2, 0],
    "bc": [2, 1],
    "br": [2, 2],
}


def main_2():
    display_grid(grid_box)
    n = 0
    while n < 9:
        i = char[n % 2]
        pos = input(f"Enter the position for player {i}: tl/cc/br?")
        pos = pos.lower()
        pos = "".join(sorted(pos))
        tmp = positions.get(pos)
        if tmp == None:
            print("Please enter a valid position!")
            continue
        row = tmp[0]
        col = tmp[1]
        if grid_box[row][col]:
            print("Please enter a valid empty position!")
            continue
        grid_box[row][col] = i
        n += 1
        display_grid(grid_box)
        if n >= 4:
            if state_of(grid_box):
                break
    else:
        print("Its a draw")

    print("Thank you for playing!")


if __name__ == "__main__":
    main_2()
