import numpy as np
from typing import List, Tuple


class PolylineFactory:

    _xc: float
    _yc: float
    _a: float
    _b: float
    _theta: float
    _n_points: int

    def __init__(self, xc: float, yc: float, a: float, b: float, theta: float, n_points: int):
        self._xc = xc
        self._yc = yc
        self._a = a
        self._b = b
        self._theta = theta
        self._n_points = n_points

    def buildPolyline(self) -> List[Tuple[int, int]]:
        t = np.linspace(0, 2 * np.pi, self._n_points)
        cos_t, sin_t = np.cos(self._theta), np.sin(self._theta)
        x_ellipse = self._xc + self._a * np.cos(t) * cos_t - self._b * np.sin(t) * sin_t
        y_ellipse = self._yc + self._a * np.cos(t) * sin_t + self._b * np.sin(t) * cos_t
        return list(zip(x_ellipse, y_ellipse))
    
    def _rotate_and_scale(self, x: float, y: float) -> Tuple[float, float]:
        cos_t, sin_t = np.cos(self._theta), np.sin(self._theta)
        x_rot = cos_t * x + sin_t * y
        y_rot = -sin_t * x + cos_t * y
        return x_rot, y_rot
        
    def generateInsidePoints(self, n: int) -> List[Tuple[int, int]]:
        inside_points = []
        while len(inside_points) < n:
            x_rand, y_rand = np.random.uniform(-self._a, self._a), np.random.uniform(-self._b, self._b)
            x_rot, y_rot = self._rotate_and_scale(x_rand, y_rand)
            if (x_rot / self._a) ** 2 + (y_rot / self._b) ** 2 <= 1:
                inside_points.append((self._xc + x_rot, self._yc + y_rot))
        return inside_points
    
    def generateOutsidePoints(self, n: int) -> List[Tuple[int, int]]:
        outside = []
        while len(outside) < n:
            x_rand, y_rand = np.random.uniform(-self._a, self._a), np.random.uniform(-self._b, self._b)
            x_rot, y_rot = self._rotate_and_scale(x_rand, y_rand)
            if (x_rot / self._a) ** 2 + (y_rot / self._b) ** 2 > 1:
                outside.append((self._xc + x_rot, self._yc + y_rot))
        return outside