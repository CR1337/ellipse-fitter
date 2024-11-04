# EllipseFitter

This is a small tool to fit an ellipse to a polyline and then determine if any point lies inside or outside of this ellipse.

## Setup

Clone this repository and cd into it.
```
git clone https://github.com/CR1337/ellipse-fitter.git && cd ellipse-fitter
```

Create and activate a virtual environment.
```
python3 -m venv .venv && source .venv/bin/activate
```

Install the requirements.
```
pip3 install -r requirements.txt
```

## Usage

```python
from ellipse_fitter import EllipseFitter

# This is a polyline approximating an ellipse, consisting of tuples of x- and y-values.
polyline = [(-1, -1), (1, -1), (1, 1), (-1, 1)]

# Instantiate an EllipseFitter.
fitter = EllipseFitter(polyline)

# Now you can check if a point is inside the ellipse.
is_inside = fitter.contains_point(0, 0)
assert is_inside == True

is_inside = fitter.contains_point(10, 10)
assert is_inside == False
```
