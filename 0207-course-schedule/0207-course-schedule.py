from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        WHITE, GREY, BLACK = 0, 1, 2

        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[b].append(a)

        colors = [WHITE] * numCourses
        
        def is_cycle(course):
            if colors[course] == BLACK:
                return False
            if colors[course] == GREY:
                return True

            colors[course] = GREY
            for next_course in graph[course]:
                if is_cycle(next_course):
                    return True
            colors[course] = BLACK
            return False


        for course in range(numCourses):
            if colors[course] == WHITE:
                if is_cycle(course):
                    return False
        return True
