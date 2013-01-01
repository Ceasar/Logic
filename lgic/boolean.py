"""
List of common boolean function.
"""


def NOT(a):
    return not a


def AND(a, b):
    """Both a and b."""
    return a and b


def NAND(a, b):
    """Not a and b."""
    return not (a and b)


def OR(a, b):
    """Either a nor b."""
    return a or b


def NOR(a, b):
    """Neither a nor b."""
    return not (a or b)


def XOR(a, b):
    """Exclusively a or b"""
    return a != b


def XNOR(a, b):
    """Exclusively not a or b"""
    # same as biconditional
    return a == b


def IMPLIES(p, q):
    """Material conditional. if p then q."""
    return not p or q
