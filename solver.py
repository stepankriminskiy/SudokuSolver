grid = [
    [0, 0, 7, 2, 0, 0, 0, 9, 0],
    [0, 0, 6, 0, 3, 0, 7, 0, 1],
    [4, 0, 0, 0, 0, 0, 0, 6, 0],
    [1, 0, 0, 4, 9, 0, 0, 0, 7],
    [0, 0, 0, 5, 0, 8, 0, 0, 0],
    [8, 0, 0, 0, 2, 7, 0, 0, 5],
    [0, 7, 0, 0, 0, 0, 0, 0, 9],
    [2, 0, 9, 0, 8, 0, 6, 0, 0],
    [0, 4, 0, 0, 0, 9, 3, 0, 8],
] 


def DrawBoard(g):
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("---------------------------")
        for tile in range(9):
            if tile == 8:
                print(g[row][tile])
            else:
                print(g[row][tile], end=" ")
                if (tile + 1) % 3 == 0:
                    print(" | ", end=" ")


def FindTile(g):
    for row in range(9):
        for tile in range(9):
            if g[row][tile] == 0:
                return (row, tile)


def valid(g, num, pos):
    for i in range(9):
        if g[pos[0]][i] == num:
            return False
        if g[i][pos[1]] == num:
            return False

        box_x = pos[1] // 3
        box_y = pos[0] // 3

    for i in range(box_y * 3, (box_y * 3) + 3):
        for j in range(box_x * 3, (box_x * 3) + 3):
            if g[i][j] == num:
                return False
    else:
        return True


def solve(g):
    pos = FindTile(g)
    if pos is None:
        return True

    for i in range(1, 10):
       if valid(g, i, pos):
            g[pos[0]][pos[1]] = i
            print(" ")
            DrawBoard(g)
            if solve(g):
                return True

            g[pos[0]][pos[1]] = 0
    return False



solve(grid)
