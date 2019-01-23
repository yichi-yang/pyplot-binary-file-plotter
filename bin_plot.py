import numpy as np
import matplotlib.pyplot as pp
import sys

assert len(sys.argv) >= 3
data = np.fromfile(sys.argv[1], dtype=sys.argv[2])

if(len(sys.argv) >= 5):
    trim_left = 0 if sys.argv[3] == "None" else int(sys.argv[3])
    trim_right = data.size if sys.argv[4] == "None" else int(sys.argv[4])
    assert trim_left < trim_right
    data = data[trim_left:trim_right]

pp.plot(np.arange(data.shape[0]), data, 'r,')
pp.plot(np.arange(data.shape[0]), data, 'r-', alpha = 0.1)
pp.show()
