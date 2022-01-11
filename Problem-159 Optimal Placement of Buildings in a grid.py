# Optimal Placement of Buildings in a grid

# Logic: We make all the possible arrangements of build placements. 
# For every possible placement, we calculate the farthest plot by 
# using BFS. We take buildings as independent nodes. The number of 
# levels in BFS will tell us farthest plot in an arrangement.

# Time Complexity: O(exponential)
# Space Complexity: O(height * width)

from collections import deque
class BuildingPlacement:
    def __init__(self) -> None:
        self.result = float('inf')
    
    def bfs(self, plots, height, width):
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        q = deque()
        lvl = 0

        # Add all the buildinging in the q
        for i in range(height):
            for j in range(width):
                if plots[i][j] == -1:
                    q.append((i,j))
                    visited.add((i,j))

        while q:
            size = len(q)

            for i in range(size):
                row, col = q.popleft()

                for _dir in dirs:
                    newRow = row + _dir[0]
                    newCol = col + _dir[1]

                    if 0 <= newRow < height and 0 <= newCol < width and (newRow, newCol) not in visited:
                        q.append((newRow, newCol))
                        visited.add((newRow, newCol))
            lvl += 1

        self.result = min(self.result, lvl-1)

    def backtrack(self, plots, height, width, buildings, row, col):
        # Base cases
        if buildings == 0:
            self.bfs(plots, height, width)
            return
        
        if col == width:
            row += 1
            col = 0

        for i in range(row, height):
            for j in range(col, width):
                plots[i][j] = -1

                self.backtrack(plots, height, width, buildings - 1, i, j + 1)

                plots[i][j] = 0

    def findMinDistance(self, height, width, buildings):
        plots = [[0 for i in range(width)] for j in range(height)]

        self.backtrack(plots, height, width, buildings, 0, 0)
        return self.result

obj = BuildingPlacement()
print(obj.findMinDistance(4, 4, 3))