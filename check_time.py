#!/usr/bin/env python
# -*- coding: utf-8 -*-
# written by Christoph Federrath, 2019-2022

import os, sys
import numpy as np
import argparse
import timeit
import tempfile
import subprocess
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patheffects as path_effects
import matplotlib.patches as patches
from matplotlib import rcParams
try:
    import cmasher as cmr
except:
    pass
import flashlib as fl
import cfpack.constants as const
import cfpack as cfp
from cfpack import print, hdfio, stop

# =============== flashplotlib class ===============

verbose = 1
direction = 'z'
bounds = None
plotlabel = ''
unitsystem = 'CGS'
redshift = None # for cosmology
convert2proper = False # convert co-moving quantities to proper quantities (for cosmology)
time = None
time_unit = None
time_scale = None
time_format = None
time_transform = 'q'
axes_label = [None, None, None]
axes_unit = [None, None, None]
axes_format = [None, None, None]
axes_transform = ['q', 'q', 'q']
data_transform = 'q'
log = True
facecolor = None
colorbar = "True" # can also be 0, "None", "False" to turn off, or "only" to make only the colorbar
cmap = 'afmhot' # 'magma'
cmap_label = None
cmap_format = None
vmin = None
vmax = None
pixel = None
shift = None
shift_periodic = None
boundary = 'isolated' # can also be 'periodic'
gauss_smooth_fwhm = [None, None]
scale_sinks_by_mass = False
show_sinks = False
show_tracers = None
particle_color = None
particle_size_factor = 1.0
particle_mark_tags = ["particle_mark_tags.h5", 'blue', 2.0] # [HDF5-file-with-tags, color, particle-size-factor]
vec = False
vec_transform = 'q'
vec_var = 'vel'
vec_scale = None
vec_scale_factor = 1.0
vec_n = [None, None]
vec_color = 'black'
stream = False
stream_transform = 'q'
stream_var = 'mag'
stream_vmin = None
stream_thick = 1.0
stream_n = [None, None]
stream_color = 'blue'
show_blocks = None
show_grid = None
bb = None # block bounding boxes
rl = None # block refinement levels
nb = None # number of cells per block
outtype = ['screen']
outname = None
# init some matplotlib parameters
rcParams['text.usetex'] = True
rcParams['text.latex.preamble'] = r'\usepackage{bm}'
rcParams['xtick.top'] = True
rcParams['xtick.direction'] = 'in'
rcParams['xtick.minor.visible'] = True
rcParams['ytick.right'] = True
rcParams['ytick.direction'] = 'in'
rcParams['ytick.minor.visible'] = True
rcParams['axes.linewidth'] = 0.5
rcParams['xtick.major.width'] = 0.5
rcParams['xtick.minor.width'] = 0.5
rcParams['ytick.major.width'] = 0.5
rcParams['ytick.minor.width'] = 0.5
rcParams['font.size'] = 10
# ============= end: __int__ =============

# ============= particles class =============rticles ==============

# ============= text class =============

# ============= end: text ==============

# ============= transform_quantity =============
def transform_quantity(q, string_expression):
# evaluate string expression containing 'q' (e.g. "2*q-0.5")
    return eval(string_expression)
# ============= end: transform_quantity =============

# ============= get_map_var =============
def get_map_var(filename=None, datasetname=None):
    if filename is None:
        print("Error. Must specify filename.")
        exit()
    if datasetname is None:
        print("Error. Must specify datasetname.")
        exit()
    # read 2D dataset
    if verbose > 1: print("Now reading data...")
    # dataset is derived or is an expression
    if type(datasetname) == list:
        if datasetname[0].find('derived:oadv') == 0:
            oadv = hdfio.read(filename[1], datasetname[1])
            dens = hdfio.read(filename[2], datasetname[2])
            map_var = oadv * dens
            datasetname = 'derived_oadv'
            filename = filename[-1] # pass the last one
    else:
        map_var = hdfio.read(filename, datasetname)
        filename = filename
        datasetname = datasetname
    return transform_quantity(map_var, data_transform)
# ============= end: get_map_var =============

# ============= prep_map =============
def prep_map(filename=None, datasetname=None):
    # map variable
    if verbose > 1: print("Getting map variable...")
    data = get_map_var(filename=filename, datasetname=datasetname)
    # time
    
    # format and scale the time
    def format_time(time_in_sec):
        if time_scale == 0: return '' # if we don't want to display time at all
        tsign = np.sign(time_in_sec)
        t = abs(time_in_sec)
        if time_transform != 'q':
            tsign = 1
            t = transform_quantity(time_in_sec, time_transform)
            time_unit = ''
        if time_unit is None: # automatic
            if t <= 1e-10: return r"$0$" # return a "0" string if time is really small
            if 1e-10 < t <= 1e-6: time_unit = 'ns'
            elif 1e-6 < t <= 1e7: time_unit = 's'
            elif 1e7 < t <= 1e11: time_unit = 'yr'
            elif 1e11 < t: time_unit = 'Myr'
            else: time_unit = 's'
        if time_scale is None: # automatic
            if time_unit.lower() == 'ns': time_scale = 1e-9
            elif time_unit.lower() == 'yr': time_scale = const.year
            elif time_unit.lower() == 'myr': time_scale = 1e6*const.year
            else: time_scale = 1.0
        if time_format is None: time_str = str(cfp.round(t/time_scale*tsign,3))
        else:
            time_str = "{:"+time_format+"}"
            time_str = time_str.format(t/time_scale*tsign)
        return r"$"+time_str+"\,\mathrm{"+time_unit+"}$"
    # read time
    time = hdfio.read(filename, "time")[0]
    if time is None:
        time_str = format_time(time)
        
        
        print(time_str)
            
filename = f'Turb_hdf5_plt_cnt_0001'
datasetname = f'dens'

prep_map(filename,datasetname)

import os

# wd=os.chdir('pah of your working directory') #change the file path to your working directory
# wd=os.getcwd() #request what is the current working directory
# print(wd)

if __name__ == '__main__':
    # import required libraries
    import h5py as h5
    import numpy as np
    import matplotlib.pyplot as plt

    f = h5.File('Turb_hdf5_plt_cnt_0001', "r")
    datasetNames = [n for n in f.keys()]
    for n in datasetNames:
        print(n)
        
        
        
        

import h5py

filename = "Turb_hdf5_plt_cnt_0001"

h5 = h5py.File(filename,'r')

futures_data = h5['sim info'] 
print(futures_data)