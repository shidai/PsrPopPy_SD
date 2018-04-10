#!/usr/bin/python

import os

import math
import random

import ctypes as C
from numpy.ctypeslib import ndpointer

# Edited by Shi Dai, 2017/03/22
import subprocess
import re
import numpy as np

__libdir__ = '/Users/dai02a/Soft/psrpop/PsrPopPy_test/lib/'
ymwpath = os.path.join(__libdir__, 'ymw16')
ymw16lib = C.CDLL('/Users/dai02a/Soft/psrpop/PsrPopPy_test/lib/ymw16/ymw16lib.so')
#ymw16lib.dm_.restype = C.c_float

gl = 120.0
gb = 10.0
dist = 1.0  # kpc

proc = subprocess.Popen(['/Users/dai02a/Soft/psrpop/PsrPopPy_test/lib/ymw16/ymw16', '-d', '/Users/dai02a/Soft/psrpop/PsrPopPy_test/lib/ymw16/', 'Gal', str(gl), str(gb), str(1000.0*dist), str(2)], shell=False, stdout=subprocess.PIPE)
lines = proc.stdout.readlines()
numbers = re.findall("[-+]?\d+[\.]?\d*[eE]?[-+]?\d*", lines[0])
if len(numbers) == 5:
    dm = float(numbers[3])
    tau = 1000.0*np.power(10.0, float(numbers[4]))    # ms
else:
    print "YMW16 doesn't work...\n"

print dm, tau

gl = 120.0
gb = 10.0
dist = 1.0  # kpc

dist = C.c_double(1000*dist)
gl = C.c_double(gl)
gb = C.c_double(gb)
#ymw16type = C.c_int(2)
#ymw16model = C.c_char_p("Gal")
#inpath = C.create_string_buffer(ymwpath)
#linpath = C.c_int(len(ymwpath))

#ymw16lib.myprint()
#print ymw16lib.myadd(gl, gb)
ymw16lib.run_ymw16.restype = C.c_double
dm1 = ymw16lib.run_ymw16(gl,gb,dist)
print dm1

'''
dm = ymw16lib.dm_(C.byref(dist),
                 C.byref(gl),
                 C.byref(gb),
                 C.byref(C.c_int(4)),
                 C.byref(C.c_float(0.0)),
                 C.byref(inpath),
                 C.byref(linpath))
        tau = scatter_bhat(dm, scatterindex=-3.86, freq_mhz=1400.0)
'''
