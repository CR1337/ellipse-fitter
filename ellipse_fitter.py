import numpy as np
from scipy.optimize import least_squares
from typing import List, Tuple


Params = Tuple[float, float, float, float, float]


class EllipseFitter:

    _polyline: List[Tuple[int, int]]

    _xc: float  # x-coordinate of the center
    _yc: float  # y-coordinate of the center
    _a: float  # semi-major axis
    _b: float  # semi-minor axis
    _theta: float  # rotation angle

    def __init__(self, polyline: List[Tuple[int, int]]):
        self._polyline = polyline
        self._xc, self._yc, self._a, self._b, self._theta = self._fit()

    def _ellipse_residual(self, params: Params, x: float, y: float) -> float:
        xc, yc, a, b, theta = params
        cos_t, sin_t = np.cos(theta), np.sin(theta)
        x_rot = cos_t * (x - xc) + sin_t * (y - yc)
        y_rot = -sin_t * (x - xc) + cos_t * (y - yc)
        return ((x_rot / a) ** 2 + (y_rot / b) ** 2 - 1)

    def _fit(self) -> Params:
        x, y = zip(*self._polyline)
        x_mean, y_mean = np.mean(x), np.mean(y)
        initial_guess = [x_mean, y_mean, (max(x) - min(x)) / 2, (max(y) - min(y)) / 2, 0]
        result = least_squares(self._ellipse_residual, initial_guess, args=(np.array(x), np.array(y)))
        return result.x
    
    def contains_point(self, x: int, y: int) -> bool:
        cos_t, sin_t = np.cos(self._theta), np.sin(self._theta)
        x_rot = cos_t * (x - self._xc) + sin_t * (y - self._yc)
        y_rot = -sin_t * (x - self._xc) + cos_t * (y - self._yc)
        return (x_rot / self._a) ** 2 + (y_rot / self._b) ** 2 <= 1
