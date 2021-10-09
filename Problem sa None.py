# Problem sa provjerom None javlja exception
INITIAL = object()  # completely unique value

# workaruond:

INITIAL = object()

def min(iterable, default=INITIAL):
    """Imperfect re-implementation of Python's built-in min function."""
    minimum = INITIAL
    for item in iterable:
        if minimum is INITIAL or item < minimum:
            minimum = item
    if minimum is not INITIAL:
        return minimum
    elif default is not INITIAL:
        return default
    else:
        raise ValueError("Empty iterable")

Even an empty list:
	
INITIAL = []


def min(iterable, default=INITIAL):
    """Imperfect re-implementation of Python's built-in min function."""
    minimum = INITIAL
    for item in iterable:
        if minimum is INITIAL or item < minimum:
            minimum = item
    if minimum is not INITIAL:
        return minimum
    elif default is not INITIAL:
        return default
    else:
        raise ValueError("Empty iterable")


from itertools import zip_longest

SENTINEL = object()

def strict_zip(*iterables):
    """Variation of ``zip`` which requires equal-length iterables."""
    for values in zip_longest(*iterables, fillvalue=SENTINEL):
        if SENTINEL in values:
            raise ValueError("Given iterables must have the same length.")
        yield values
