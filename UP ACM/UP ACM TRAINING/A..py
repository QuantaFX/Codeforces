#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'place_magic_stones' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER height
#  2. INTEGER width
#  3. INTEGER_ARRAY rows
#  4. INTEGER_ARRAY columns
#  5. INTEGER_ARRAY colors
#  6. INTEGER_ARRAY rows_to_place
#  7. INTEGER_ARRAY columns_to_place
#  8. INTEGER_ARRAY colors_to_place

# height, width (col, row)
# (rows, colums = colors) (already there)
# (rows, colums = colors) to place (to be placed)

# 40% is just 1 <= height, width <= 10
# first submission 4/20
# target subtast first

def place_magic_stones(height, width, rows, columns, colors, rows_to_place, columns_to_place, colors_to_place):

    # Key : (r, x)
    grid = {}
    # Place initial Stones
    for i in range(len(rows)):
        grid[(rows[i], columns[i])] = colors[i]

    answer = []
    # Simulate the placing
    for p in range(len(rows_to_place)):
        R = rows_to_place[p]
        C = columns_to_place[p]
        COL = colors_to_place[p]
        # Place the new stone
        grid[(R, C)] = COL

        end_stones = {}
        for (r, c), col in grid.items():
            if col != COL:
                continue
            dr = r - R
            dc = c - C
            if dr == 0 and dc == 0:
                continue
            # Check 8 directions
            if dr == 0 or dc == 0 or abs(dr) == abs(dc):
                # Normalize to -1, 1, 0
                dir_r = dr // abs(dr) if dr != 0 else 0
                dir_c = dc // abs(dc) if dc != 0 else 0
                direction = (dir_r, dir_c)
                dist = max(abs(dr), abs(dc))
                if direction not in end_stones or dist < end_stones[direction]:
                    end_stones[direction] = dist

        flip = []
        for (r, c), col in grid.items():
            if col == COL:
                continue

            dr = r - R
            dc = c - C
            if dr == 0 or dc == 0 or abs(dr) == abs(dc):
                # Normalize to -1, 1, 0
                dir_r = dr // abs(dr) if dr != 0 else 0
                dir_c = dc // abs(dc) if dc != 0 else 0
                direction = (dir_r, dir_c)
                dist = max(abs(dr), abs(dc))
                if direction in end_stones and dist < end_stones[direction]:
                    flip.append((r, c))

        for r, c in flip:
            grid[(r, c)] = COL
        answer.append(len(flip))
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    height = int(input().strip())

    width = int(input().strip())

    rows_count = int(input().strip())

    rows = []

    for _ in range(rows_count):
        rows_item = int(input().strip())
        rows.append(rows_item)

    columns_count = int(input().strip())

    columns = []

    for _ in range(columns_count):
        columns_item = int(input().strip())
        columns.append(columns_item)

    colors_count = int(input().strip())

    colors = []

    for _ in range(colors_count):
        colors_item = int(input().strip())
        colors.append(colors_item)

    rows_to_place_count = int(input().strip())

    rows_to_place = []

    for _ in range(rows_to_place_count):
        rows_to_place_item = int(input().strip())
        rows_to_place.append(rows_to_place_item)

    columns_to_place_count = int(input().strip())

    columns_to_place = []

    for _ in range(columns_to_place_count):
        columns_to_place_item = int(input().strip())
        columns_to_place.append(columns_to_place_item)

    colors_to_place_count = int(input().strip())

    colors_to_place = []

    for _ in range(colors_to_place_count):
        colors_to_place_item = int(input().strip())
        colors_to_place.append(colors_to_place_item)

    result = place_magic_stones(height, width, rows, columns, colors, rows_to_place, columns_to_place, colors_to_place)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
