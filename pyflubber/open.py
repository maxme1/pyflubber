import numpy as np
from .points import get_fractions, interpolate_along_axis


def prepare(start: np.ndarray, stop: np.ndarray):
    # handling a possible flip
    diff = np.linalg.norm(start[[0, -1]] - stop[[0, -1]], axis=1).sum()
    rev_diff = np.linalg.norm(start[[-1, 0]] - stop[[0, -1]], axis=1).sum()
    if rev_diff < diff:
        start = start[::-1]

    start_fractions = get_fractions(start)
    stop_fractions = get_fractions(stop)
    merged = np.union1d(start_fractions, stop_fractions)

    start = interpolate_along_axis(merged, start_fractions, start)
    stop = interpolate_along_axis(merged, stop_fractions, stop)
    return start, stop
