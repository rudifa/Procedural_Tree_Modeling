


Rudolf Farkas
could you have a go and propose the 2 files modified to use python in place of cuda.jit?

Certainly! I'll provide you with modified versions of both lpy.py and Utility.py files, replacing CUDA operations with pure Python equivalents. Please note that these modifications will result in slower execution times compared to the CUDA versions.

First, let's modify the lpy.py file:

**File: /Users/rudifarkas/GitHub/uzufly/Procedural_Tree_Modeling/lpy.py**

```python
import os
import Utility
import config
import cv2
import logging
import warnings
import math
import numpy as np

numba_logger = logging.getLogger('numba')
numba_logger.setLevel(logging.WARNING)
warnings.filterwarnings('ignore')

# Remove CUDA-specific constants
# TPB = 1024
# NB = 128
MAX_NODES_SIZE = 204800

class BBox:
    # ... (keep the BBox class as is)

def compute_light_fast(buds_light_array, buds_pos_array, ls, buds_size, interval, branch_angle_bins_num, bins_num):
    for thres_idx in range(buds_size * buds_size):
        bud_idx = thres_idx // buds_size
        target_bud_idx = thres_idx % buds_size
        x, y, z, n = buds_pos_array[bud_idx]
        x2, y2, z2, n2 = buds_pos_array[target_bud_idx]
        if z2 <= z:
            continue
        dx = x2 - x
        dy = y2 - y
        dz = z2 - z
        r = math.sqrt(dx * dx + dy * dy + dz * dz)
        branch_angle = math.asin(dz / r) / math.pi * 180
        roll_angle = math.atan2(dy, dx) / math.pi * 180
        branch_angle_bin = int(branch_angle / interval) if dz != r else branch_angle_bins_num - 1
        roll_angle_bin = (int(roll_angle / interval) + bins_num) % (2 * bins_num)
        bin_index = roll_angle_bin * 3 + branch_angle_bin
        buds_light_array[bud_idx, bin_index] = max(0, buds_light_array[bud_idx, bin_index] - n2 * ls)

# Keep the CPU_compute_light_fast function as is

# ... (rest of the file remains the same)
```

Now, let's modify the Utility.py file:

**File: /Users/rudifarkas/GitHub/uzufly/Procedural_Tree_Modeling/Utility.py**

```python
import os
import numpy as np
import math

def creat_path(path):
    if not os.path.exists(path):
        os.makedirs(path)

def distance_3d(p1, p2):
    d = np.array(p1) - np.array(p2)
    return math.sqrt(d.dot(d))

def subtraction_3d(t1, t2):
    return (t1[0] - t2[0], t1[1] - t2[1], t1[2] - t2[2])

def subtraction_3d_scalar(t1, t2):
    return (t1[0] - t2, t1[1] - t2, t1[2] - t2)

def addition_3d(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1], t1[2] + t2[2])

def addition_3d_scalar(t1, t2):
    return (t1[0] + t2, t1[1] + t2, t1[2] + t2)

def division_3d(t1, t2):
    return (t1[0] / t2[0], t1[1] / t2[1], t1[2] / t2[2])

def division_3d_scalar(t1, t2):
    return (t1[0] / t2, t1[1] / t2, t1[2] / t2)

def multiplication_3d(t1, t2):
    return (t1[0] * t2[0], t1[1] * t2[1], t1[2] * t2[2])

def multiplication_3d_scalar(t1, t2):
    return (t1[0] * t2, t1[1] * t2, t1[2] * t2)

def subtraction_2d(t1, t2):
    return (t1[0] - t2[0], t1[1] - t2[1])

def subtraction_2d_scalar(t1, t2):
    return (t1[0] - t2, t1[1] - t2)

def addition_2d(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

def addition_2d_scalar(t1, t2):
    return (t1[0] + t2, t1[1] + t2)

def division_2d(t1, t2):
    return (t1[0] / t2[0], t1[1] / t2[1])

def division_2d_scalar(t1, t2):
    return (t1[0] / t2, t1[1] / t2)

def multiplication_2d(t1, t2):
    return (t1[0] * t2[0], t1[1] * t2[1])

def multiplication_2d_scalar(t1, t2):
    return (t1[0] * t2, t1[1] * t2)

def to_tuple_3d(v):
    return (v[0], v[1], v[2])

def to_tuple_2d(v):
    return (v[0], v[1])

def cross_3d(v1, v2):
    x = v1[1] * v2[2] - v1[2] * v2[1]
    y = v1[2] * v2[0] - v1[0] * v2[2]
    z = v1[0] * v2[1] - v1[1] * v2[0]
    return (x, y, z)

def dot_3d(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]

def length_3d(v):
    return math.sqrt(dot_3d(v, v))

def normalize_3d(v):
    l = length_3d(v)
    return (v[0] / l, v[1] / l, v[2] / l)

def get_3d_line_plane_cross(plane_para, line_para):
    a, b, c, x1, y1, z1 = plane_para
    d, e, f, x2, y2, z2 = line_para
    vpt = d * a + e * b + f * c
    if vpt == 0:
        return (x2, y2, z2), 0.0
    t = ((x1 - x2) * a + (y1 - y2) * b + (z1 - z2) * c) / vpt
    return (x2 + t * d, y2 + t * e, z2 + t * f), t

# ... (keep the rest of the utility functions as they are)
```

These modifications replace the CUDA-specific operations with standard Python equivalents. The main changes include:

1. Removing CUDA-specific decorators and imports.
2. Replacing CUDA kernel functions with regular Python functions.
3. Removing device-specific code and replacing it with CPU-based calculations.

Please note that these changes will result in slower execution times, especially for large datasets, as they don't utilize GPU acceleration. However, they should work correctly on systems without CUDA support.
