# 3D Game of Life
*summary by Claus*

Last month Imy was looking into 3D versions of the game of life. Out
of several projects, [Cubic Life](https://github.com/xms0g/cubicLife)
looked the best.

![3D Game of Life animation](images/3DGOL.gif)

The rules are rather simple: Out of the 26 neighbors (+/-1 in all 3D
directions), a live cell dies with less than 5 or more than 6
neighbors, and a dead cell is born with exactly 4 neighbors.
