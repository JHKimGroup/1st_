def lowerBound(arr, target) -> int:
    start = 1
    end = len(arr)

    while (end > start):
        mid = (start + end) // 2
        if (arr[mid] < target):
            start = mid + 1
        else:
            end = mid
    return end + 1


def upperBound(arr, target) -> int:
    start = 1
    end = len(arr)

    while (end > start):
        mid = (start + end) // 2
        if (arr[mid] <= target):
            start = mid + 1
        else:
            end = mid
    return end + 1


class Solution(object):
    seg_tree = []
    start_point = 1
    end_point = 0

    def __init__(self, points):
        now_points = sorted(points, key=lambda x: (x[0], x[1]))

        for [x, y] in (now_points):
            if self.end_point < x:
                self.end_point = x
        self.end_point += 1

        self.make_tree(now_points, self.start_point, self.end_point)

        # print (self.seg_tree)
        """
        Initialize this class instance.

        Parameters
        ----------
        points : list of integer coordinates, each of form [x,y], that is
                 [[x1,y1], [x2,y2], ... , [xN,yN]]
        """
        pass

    def make_tree(self, points, start, end):

        for i in range(end * 4):
            self.seg_tree.append([0])

        for [x, y] in (points):
            self.insert_tree(start, end, 1, x + 1, y)

        # print (tree)

        self.merge_tree(start, end, 1)

        # print (tree)

    def merge_tree(self, start, end, node):
        mid = (start + end) // 2
        if start == end:
            return

        self.merge_tree(start, mid, node * 2)
        self.merge_tree(mid + 1, end, node * 2 + 1)

        # print (start, end)
        left_child_size = len(self.seg_tree[node * 2])
        right_child_size = len(self.seg_tree[node * 2 + 1])
        left_pivot = 1
        right_pivot = 1

        while left_child_size > left_pivot or right_child_size > right_pivot:
            if left_child_size <= left_pivot:
                self.seg_tree[node].append(self.seg_tree[node * 2 + 1][right_pivot])
                right_pivot += 1
            elif right_child_size <= right_pivot:
                self.seg_tree[node].append(self.seg_tree[node * 2][left_pivot])
                left_pivot += 1
            else:
                if self.seg_tree[node * 2 + 1][right_pivot] > self.seg_tree[node * 2][left_pivot]:
                    self.seg_tree[node].append(self.seg_tree[node * 2][left_pivot])
                    left_pivot += 1
                else:
                    self.seg_tree[node].append(self.seg_tree[node * 2 + 1][right_pivot])
                    right_pivot += 1

    def insert_tree(self, start, end, node, target, value):
        mid = (start + end) // 2
        # print (node, mid, start, end)
        if start == target and end == target:
            self.seg_tree[node].append(value)
            return

        if end < target or target < start:
            return

        self.insert_tree(start, mid, node * 2, target, value)
        self.insert_tree(mid + 1, end, node * 2 + 1, target, value)

    def query(self, rect) -> int:
        rect[0][1] += 1
        rect[0][0] += 1

        # print (self.seg_tree)

        Answer = self.operate_query(rect)
        return Answer;

        """
        Find the number of points within the given rectangle

        Parameters
        ----------
        rect: [[xL,xR], [yL,yR]]
              where xL, xR, yL and yR are integers with xL <= xR and yL <= yR

        Returns
        -------
        int
            the number of point (x, y)
            such that xL <= x <= xR and yL <= y <= yR
        """
        pass

    def operate_query(self, rect):
        start = self.start_point
        end = self.end_point

        return self.search_tree(start, end, 1, rect)

    pass

    def search_tree(self, start, end, node, rect) -> int:
        mid = (start + end) // 2
        left = rect[0][0]
        right = rect[0][1]

        if end < left or right < start:
            return 0

        if left <= start and end <= right:

            point_start = lowerBound(self.seg_tree[node], rect[1][0])
            point_end = upperBound(self.seg_tree[node], rect[1][1])
            """print (rect[1][0], rect[1][1])
            print (point_start, point_end,"시작" , start, "끝", end)
            print (tree[node])"""

            if point_start >= point_end:
                return 0
            else:
                return (point_end - point_start)

        return self.search_tree(start, mid, node * 2, rect) + self.search_tree(mid + 1, end, node * 2 + 1, rect)

    pass


"""
f = open("input.txt", 'r')

T = int(f.readline())

for i in range (1,T + 1):
    P, Q = map(int, f.readline().split())

    points = []
    for j in range (1, P + 1):
        a, b = map(int, f.readline().split())
        points.append([a, b])
    sol = Solution(points)

    Answer = 0
    for j in range (1, Q + 1):
        a, b, c, d = map(int, f.readline().split())
        Answer += sol.query ([[a, b], [c, d]])

    print (Answer)

    points.clear()
    sol.seg_tree.clear()
    sol.start_point = 1
    sol.end_point = 0
"""

T = int(input())

for i in range(1, T + 1):
    P, Q = map(int, input().split())

    points = []
    for j in range(1, P + 1):
        a, b = map(int, input().split())
        points.append([a, b])
    sol = Solution(points)

    Answer = 0
    for j in range(1, Q + 1):
        a, b, c, d = map(int, input().split())
        Answer += sol.query([[a, b], [c, d]])

    print(Answer)

    points.clear()
    sol.seg_tree.clear()
    sol.start_point = 1
    sol.end_point = 0