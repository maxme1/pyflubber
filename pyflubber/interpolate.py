from typing import Union, Iterable, Sequence, Callable

import numpy as np

from .closed import prepare as prepare_closed
from .open import prepare as prepare_open

Line = Union[np.ndarray, Iterable[Sequence[float]]]


def _normalize_parameter(t):
    if not (0 <= t <= 1):
        raise ValueError('The interpolation parameter must be between 0 and 1.')

    return t


def _normalize_line(line):
    assert len(line) > 0
    line = np.asarray(line)
    assert line.ndim == 2
    # TODO: remove duplicates
    return line


def interpolate(start: Line, stop: Line, t: float, closed: bool = True) -> np.ndarray:
    """
    Interpolate between ``start`` and ``stop`` according to interpolation parameter ``t``.

    Parameters
    ----------
    start: numpy.ndarray
        the starting line. Expected shape (N, d),
        where N is the number of points and d - their dimensionality.
    stop: numpy.ndarray
        the ending line. Expected shape (M, d),
        where M is the number of points and d - their dimensionality.
    t: float
        the interpolation parameter. Must be between 0 and 1.
    closed: bool
        whether the lines are closed

    Returns
    -------
    interpolated_line: numpy.ndarray

    Notes
    -----
    The number of points in each line are not necessarily equal.
    In case of closed lines only 2D points are supported.
    """
    t = _normalize_parameter(t)
    return interpolator(start, stop, closed)(t)


def interpolator(start: Line, stop: Line, closed: bool = True) -> Callable:
    """
    Returns a function that interpolates between ``start`` and ``stop`` given an interpolation parameter.

    Parameters
    ----------
    start: numpy.ndarray
        the starting line. Expected shape (N, d),
        where N is the number of points and d - their dimensionality.
    stop: numpy.ndarray
        the ending line. Expected shape (M, d),
        where M is the number of points and d - their dimensionality.
    closed: bool
        whether the lines are closed

    Returns
    -------
    interpolator: a function that given the interpolation parameter t
        returns the interpolated line.
    """

    def interpolate_(t: float):
        t = _normalize_parameter(t)
        return start + delta * t

    prepare = prepare_closed if closed else prepare_open
    start, stop = prepare(_normalize_line(start), _normalize_line(stop))
    delta = stop - start

    return interpolate_
