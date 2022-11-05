number_grids = [[1, 2, 3, 4], [3, 4, 5, 6], [9, 8, 7, 6]]

print()
print(number_grids[2][0], "is the first element of the third")
print()

for row in number_grids:
    for col in row:
        print(col)
