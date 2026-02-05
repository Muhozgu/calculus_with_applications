import sys
import os
sys.path.insert(0, 'exercises/slope')

from exercises.slope.equation import find_d2p 

def sales(x1, y1, x2, y2):
    return find_d2p(x1, y1, x2, y2)

print(sales(2, 27, 5, 63))