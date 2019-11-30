import numpy as np


def get_fractions(line):
    fractions = np.linalg.norm(np.diff(line, axis=0), axis=1).cumsum()
    fractions /= fractions[-1]
    return np.insert(fractions, 0, 0)


def interpolate_along_axis(new_coords, coords, values):
    return np.stack([np.interp(new_coords, coords, v) for v in values.T], 1)
