import h5py
import numpy as np
f = h5py.File('D:/1.h5 ', 'r')

for key in f.keys():
    print(f[key].name)
a = f.attrs['layer_names'][0]

print(list(f['predictions']))

b = f['predictions/predictions_W_1:0'].value
