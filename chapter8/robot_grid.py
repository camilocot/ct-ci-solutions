# Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
# The robot can only move in two directions, right and down, but certain cells are "off limits" such that
# the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
# the bottom right.

# Intuition: If we picture this grid, the only way to move to spot ( r, c) is by moving to one of the adjacent spots:
# (r - 1, c) or (r, c - 1). So, we need to find a path to either(r-1, c) or (r, c - 1).
# So then, to find a path from the origin, we just work backwards like this.

# Brute force
# This solution is O ( 2^r+c), since each path has r+c steps and there are two choices we can make at each step.

# Dinamic Prodaming - failed track
# The algorithm will now take O(rc) time because we hit each cell just once.


def find_path(maze):
    def helper(maze, r, c, path, failed):

        # If out of bounds or not available
        if r < 0 or c < 0 or not maze[c][r] or (r, c) in failed:
            return False

        is_at_origin = (r == 0) and (c == 0)

        # If there's a path from the start to here, add my location.
        if is_at_origin or helper(maze, r, c-1, failed) or helper(maze, r-1, c, failed):
            maze.append((r, c))
            return True

        # Cache result
        failed.append((r, c))
        return False

    if len(maze) == 0 or len(maze[0]) == 0:
        return None

    path = []
    # Track if we've already visited this cell
    failed = []
    if helper(maze, len(maze) - 1, len(maze[0])-1, path, failed):
        return path
    return None
