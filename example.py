from lgic.boolean import *
from lgic.schemata import *


def one():
  print "1"

  print "a", Schema(lambda p, q, r: any((p == q, p == r, q == r))).valid
  print "b", Schema(lambda p, q: IMPLIES(p, q) or IMPLIES(q, p)).valid
  print "c", Schema(lambda p, q, r: (p != (q != r)) == ((p != q) != r)).valid


def two():
  print "2"
  print "a", Schema(lambda p, q, r: (p != r) == (q != r)).implies(Schema(lambda p, q, r: p == q))
  print "b", Schema(lambda p, q, r: p != (q == r)).implies(Schema(lambda p, q, r: (p != q) == (p != r)))
  print "c", Schema(lambda p, q: IMPLIES(q, p)).implies(Schema(lambda p, q: IMPLIES(-p, -q)))
  print "d", Schema(lambda p, q, r: (p and q) or r).implies(Schema(lambda p, q, r: p and (q or r)))
  print "e", Schema(lambda p, q, r: p and (q or r)).implies(Schema(lambda p, q, r: (p and q) or r))


def three():
  print "3"
  print sum(Schema(lambda a, b, c, d, e, f: (((a != b) != c) != d) or (e and f)).truthtable.values())



if __name__ == "__main__":
  one()
  two()
  three()
