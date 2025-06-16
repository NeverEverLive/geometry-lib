# geometry_lib

Library for calculating area of the figures

## Setup

### Poetry:
```bash
poetry add geometry
```

### pip

```bash
pip install geometry
```

### From source
```bash
git clone https://github.com/nevereverlive/geometry-lib.git
cd geometry-lib
pip install .
```



## Example

```python
from geometry import create_shape

shape = create_shape("circle", 5)
print(shape.area())  # 78.5398...

triangle = create_shape("triangle", 3, 4, 5)
print(triangle.area())  # 6.0
print(triangle.is_right_angled())  # True
```