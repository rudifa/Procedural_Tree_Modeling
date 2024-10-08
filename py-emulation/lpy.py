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
        branch_angle_bin = int(
            branch_angle / interval) if dz != r else branch_angle_bins_num - 1
        roll_angle_bin = (int(roll_angle / interval) +
                          bins_num) % (2 * bins_num)
        bin_index = roll_angle_bin * 3 + branch_angle_bin
        buds_light_array[bud_idx, bin_index] = max(
            0, buds_light_array[bud_idx, bin_index] - n2 * ls)

# Keep the CPU_compute_light_fast function as is

# ... (rest of the file remains the same)
