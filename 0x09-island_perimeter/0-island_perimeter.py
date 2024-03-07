#!/usr/bin/python3
"""
    returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """island perimenter function"""
    perimeter = 0
    for x in range(len(grid)):
        for c in range(len(grid[x])):
            if grid[x][c] == 1:
                perimeter += 4
                if x > 0 and grid[x-1][c] == 1:
                    perimeter -= 2
                if c > 0 and grid[x][c-1] == 1:
                    perimeter -= 2
    return perimeter
