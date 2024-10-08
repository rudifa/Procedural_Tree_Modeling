# Experiment with Procedure Tree Modelling

## python

Reinstalled anaconda

```
rudifarkas % python -V
Python 3.12.4

rudifarkas % conda -V
conda 24.5.0

rudifarkas % path
.
/Users/rudifarkas/opt/anaconda3/condabin
/Users/rudifarkas/opt/anaconda3/bin
...
```

## conda env

```
rudifarkas % conda create -n py39 python=3.9
```

```
rudifarkas % conda activate py39
rudifarkas % python -V
Python 3.9.20


rudifarkas % path
/Users/rudifarkas/opt/anaconda3/envs/py39/bin
.
/Users/rudifarkas/opt/anaconda3/condabin
/Users/rudifarkas/opt/anaconda3/bin
...

```

## Project dependencies

```
    Numpy
    open3d
    numba
    opencv
```

## Perform modelling

```
python modelling.py [-h] [--DATA_PATH DATA_PATH] [--OUT_PATH OUT_PATH] [--GROUND_H GROUND_H]
                [--MAX_ITERATION MAX_ITERATION]
```

```
python modelling.py --DATA_PATH data/example1/data.txt --OUT_PATH data/example1 --GROUND_H 0.0
```

```

Procedural_Tree_Modeling % python modelling.py --DATA_PATH data/example1/data.txt --OUT_PATH data/example1 --GROUND_H 0.0

Traceback (most recent call last):
File "/Users/rudifarkas/GitHub/uzufly/Procedural_Tree_Modeling/modelling.py", line 4, in <module>
import Utility
File "/Users/rudifarkas/GitHub/uzufly/Procedural_Tree_Modeling/Utility.py", line 4, in <module>
from numba import jit,njit
ModuleNotFoundError: No module named 'numba'

```

```

rudifarkas % conda install numba

...
Executing transaction: done

```

```

Procedural_Tree_Modeling % python modelling.py --DATA_PATH data/example1/data.txt --OUT_PATH data/example1 --GROUND_H 0.0                   [rudifa-experiment L|…2]
Traceback (most recent call last):
  File "/Users/rudifarkas/GitHub/uzufly/Procedural_Tree_Modeling/modelling.py", line 6, in <module>
    import lpy
  File "/Users/rudifarkas/GitHub/uzufly/Procedural_Tree_Modeling/lpy.py", line 10, in <module>
    import cv2
ModuleNotFoundError: No module named 'cv2'

```

```
Procedural_Tree_Modeling % conda install opencv
Collecting package metadata (current_repodata.json): done
Solving environment: done
...
Executing transaction: done
```

```
Procedural_Tree_Modeling % python modelling.py --DATA_PATH data/example1 --OUT_PATH data/example1 --GROUND_H 0.0
processing:NLB
processing:BAM
...
numba.cuda.cudadrv.error.CudaSupportError: Error at driver init:

CUDA driver library cannot be found.


```

```
Procedural_Tree_Modeling % conda install numba
Collecting package metadata (current_repodata.json): done
Solving environment: done
...
# All requested packages already installed.

```

```
Procedural_Tree_Modeling % conda install opencv
...
Collecting package metadata (current_repodata.json): done
Solving environment: done
...
# All requested packages already installed.

```

```
Procedural_Tree_Modeling % grep. py numba                                                                                                   [rudifa-experiment L|…2]
./lpy.py:5:from numba import cuda, float32
./lpy.py:11:numba_logger = logging.getLogger('numba')
./lpy.py:12:numba_logger.setLevel(logging.WARNING)
./Utility.py:4:from numba import jit,njit
./Utility.py:5:from numba import cuda
```

## Conclusion

It appears that we can't have `numba` on M3 Macbooks.
