import numpy as np

from .points import get_fractions, interpolate_along_axis


def prepare(start: np.ndarray, stop: np.ndarray):
    start = normalize(start)
    stop = normalize(stop)

    diff = len(start) - len(stop)
    if diff < 0:
        start = add_points(start, -diff)
    elif diff > 0:
        stop = add_points(stop, diff)

    start = rotate(start, stop)
    return start, stop


def get_area(line):
    line = np.insert(line, 0, line[-1], axis=0)
    return np.cross(line[1:], line[:-1]).sum() / 2


def normalize(line):
    if line.shape[1] != 2:
        raise ValueError('In case of closed lines only 2D points are supported.')

    if get_area(line) > 0:
        line = line[::-1]

    return line


def rotate(line, reference):
    min_, best_offset = np.inf, 0

    for offset in range(len(line)):
        deviation = np.linalg.norm(reference - np.roll(line, offset, axis=0))

        if deviation < min_:
            min_ = deviation
            best_offset = offset

    if best_offset:
        line = np.roll(line, best_offset, axis=0)

    return line


def add_points(line, n_points):
    line = np.insert(line, len(line), line[0], axis=0)
    fractions = get_fractions(line)
    new_fractions = sorted(
        list(fractions) +
        list(np.linspace(0, 1, n_points, endpoint=False) + 1 / (2 * n_points))
    )[:-1]

    return interpolate_along_axis(new_fractions, fractions, line)
