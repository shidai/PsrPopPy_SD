#!/usr/bin/python

import sys
import argparse
import math
import random

import cPickle

import matplotlib.pyplot as plt
from matplotlib.widgets import Button, RadioButtons, CheckButtons

import numpy as np

from population import Population 
from pulsar import Pulsar

f = open(sys.argv[1], 'rb')
p = Pulsar()

p = cPickle.load(f)
f.close()

#print p.size()
        
for psr in p.population:
#	print psr.period
	print psr.gl, psr.gb, psr.dm, psr.dtrue, psr.t_scatter, psr.lum_1400, psr.width_degree, psr.period, psr.spindex, psr.snr, psr.delta, psr.dead
#       if psr.dead:
#	    print psr.gl, psr.gb, psr.dm, psr.dtrue, psr.t_scatter, psr.lum_1400, psr.width_degree, psr.period, psr.spindex, psr.snr, psr.delta, psr.dead
