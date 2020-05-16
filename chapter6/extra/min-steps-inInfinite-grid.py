# You are in an infinite 2D grid where you can move in any of the 8 directions:
# You are given a sequence of points and the order in which you need to cover the points.
# Give the minimum number of steps in which you can achieve it. You start from the first point.
# Input: [(0, 0), (1, 1), (1, 2)]
# Output: 2


def min_step_inf_grid(points):
    step = 0
    for p in range(len(points)-1):

        r = abs(points[p+1][0]) - abs(points[p][0])
        c = abs(points[p+1][1]) - abs(points[p][1])

        step += max(r, c)
    return step


print(min_step_inf_grid([(0, 0), (1, 1), (1, 2)]))
