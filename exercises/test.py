from fractions import Fraction

def slope(x1, y1, x2, y2):
  s1  = y2 - y1
  s2  = x2 - x1
  x = Fraction(s1,s2)
  return x