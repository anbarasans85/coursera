# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments_):
    result = dict()
    segments_ = sorted(segments_, key=lambda x: x.end)
    p1 = Segment(start=-2, end=-1)
    for s in segments_:
        if not isoverlap(p1, s):
            result[s.end] = s
            p1 = s
    return result.keys()


def isoverlap(s1, s2):
    if (s1.end == s2.start) or \
            (s1.start >= s2.start and s1.end <= s2.end) or \
            (s1.start <= s2.start and s1.end >= s2.end) or \
            (s1.start <= s2.start) and (s1.end >= s2.start) or \
            (s1.start >= s2.start) and (s2.end <= s1.end):
            return True
    else:
        return False


if __name__ == '__main__':
    input_ = sys.stdin.read()
    n, *data = map(int, input_.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
