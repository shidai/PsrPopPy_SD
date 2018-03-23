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

print p.size()
