## pyflubber

Linear interpolation of open and closed lines.

The code for closed lines is based on the 
[flubber](https://github.com/veltman/flubber) package, hence the name.

## Installation

```bash
pip install git+https://github.com/maxme1/pyflubber.git
```

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
