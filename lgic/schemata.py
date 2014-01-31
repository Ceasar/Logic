"""

>>> P = Not(Implies(Atom("P"), Not(Atom("Q"))))
>>> Q = And(Atom("P"), Atom("Q"))
>>> print P == Q
>>> print P.implies(Q)
>>> print Q.implies(P)

"""
import itertools


class Term(object):
    @property
    def truthtable(self):
        table = {}
        values = itertools.product(*[(False, True)]* len(self.atoms))
        for value in values:
            context = dict(zip(self.atoms, value))
            table[tuple(context.items())] = self.evaluate(**context)
        return table

    @property
    def valid(self):
        return all(self.truthtable.values())

    @property
    def satisfiable(self):
        return any(self.truthtable.values())

    @property
    def unsatisfiable(self):
        return not any(self.truthtable.values())

    def implies(self, other):
        assert set(self.atoms) >= set(other.atoms)
        for k, v in other.truthtable.iteritems():
            if v and not self.truthtable[k]:
                return False
        return True

    def __eq__(self, other):
        return self.truthtable == other.truthtable


class Atom(Term):
    def __init__(self, name):
        self.name = name

    @property
    def atoms(self):
        return [self.name]

    @property
    def truthtable(self):
        return {True: True, False: False}

    def evaluate(self, **context):
        return context[self.name]

    def __repr__(self):
        return self.name


class Not(Term):
    def __init__(self, p):
        self.p = p

    @property
    def atoms(self):
        return self.p.atoms

    def evaluate(self, **context):
        return not self.p.evaluate(**context)

    def __repr__(self):
        return "(not %s)" % self.p


class Connective(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    @property
    def atoms(self):
        return self.p.atoms + self.q.atoms

class And(Term, Connective):
    def evaluate(self, **context):
        return self.p.evaluate(**context) and self.q.evaluate(**context)

    def __repr__(self):
        return "(%s and %s)" % (self.p, self.q)


class Or(Term, Connective):
    def evaluate(self, **context):
        return self.p.evaluate(**context) or self.q.evaluate(**context)

    def __repr__(self):
        return "(%s or %s)" % (self.p, self.q)


class Implies(Term, Connective):
    def evaluate(self, **context):
        return not self.p.evaluate(**context) or self.q.evaluate(**context)

    def __repr__(self):
        return "(%s => %s)" % (self.p, self.q)
