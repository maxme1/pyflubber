## pyflubber

Linear interpolation of open and closed lines for Python.

The code for closed lines is based on the 
[flubber](https://github.com/veltman/flubber) package, hence the name.

A version for Dart can be found [here](https://github.com/maxme1/dart_flubber).

## Installation


```bash
pip install pyflubber
```

or

```bash
pip install git+https://github.com/maxme1/pyflubber.git
```

or 

```bash
git clone https://github.com/maxme1/pyflubber.git
cd pyflubber
pip install -e .
```

## Usage

```python
from pyflubber import interpolate

middle = interpolate(first, second, 0.5, closed=False)
```
