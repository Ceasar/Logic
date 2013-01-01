import inspect
import itertools


class Schema(object):
    def __init__(self, func):
        self._func = func

    @property
    def args(self):
        return inspect.getargspec(self._func).args

    @property
    def truthtable(self):
        table = {}
        for inputs in itertools.product(*[(False, True) for arg in self.args]):
            table[inputs] = self._func(*inputs)
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
        assert set(self.args) >= set(other.args)
        for k, v in other.truthtable.iteritems():
            if v and not self.truthtable[k]:
                return False
        return True
