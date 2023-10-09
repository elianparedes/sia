DIM = 5
CELL = (2, 2)
RADIUS = (2 ** 0.5)


def get_neighbours(x, y, r):
    result = []

    for i in range(int(x - r), int(x + r) + 1):
        if i < 0 or i >= DIM:
            continue

        for j in range(int(y - r), int(y + r) + 1):
            if j < 0 or j >= DIM:
                continue

            distance = ((x - i) ** 2 + (y - j) ** 2) ** 0.5

            if distance <= r:
                result.append((i, j))

    return result


matrix = [[0 for _ in range(DIM)] for _ in range(DIM)]
neighbours = get_neighbours(CELL[0], CELL[1], RADIUS)
print(neighbours)
for i in range(DIM):
    for j in range(DIM):
        if (i, j) in neighbours:
            matrix[i][j] = 'X'
        else:
            matrix[i][j] = 'O'
    print(matrix[i])
