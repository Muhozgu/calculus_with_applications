# Finding an aquation of a  line given a point and a slope
from slopes import slope



def find_d(m, x1, y1):
    c = -m*x1 + y1
    d = f'{m}x'
    return f'y = {d} + {c}'


def find_d2p(x1, y1, x2, y2):
    m = slope(x1, y1, x2, y2)
    return find_d(m, x1, y1)

print(find_d2p(-1, 3, 0, 3))