# We're given a hashmap associating each courseId key with a list of courseIds values,
# which represents that the prerequisites of courseId are courseIds.
# Return a sorted ordering of courses such that we can finish all courses.

# The idea here is to do a [Topological sorting](https://en.wikipedia.org/wiki/Topological_sorting).


def course_order(coursesId):
    def dfs(course):
        if visited[course]:
            return
        c = None
        for c in coursesId[course]:
            dfs(c)

        visited[course] = True

        path.append(course)

    path = []
    visited = {}

    for key, values in coursesId.items():
        visited[key] = False

    dfs('CSC300')
    return path


print(course_order({'CSC300': ['CSC100', 'CSC200'],
                    'CSC200': ['CSC100'], 'CSC100': []}))
