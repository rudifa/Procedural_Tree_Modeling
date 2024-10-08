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
