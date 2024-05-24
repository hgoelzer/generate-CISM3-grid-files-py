# Write CISM3 grid files in CDO format

import numpy as np
from generate_CDO_files_nc import generate_CDO_files

# for checking
def isaninteger(x):
    return np.mod(x, 1) == 0

# Specify mapping information. This is EPSG 3031 for AIS
proj_info = {}
proj_info['earthradius'] = 6378137.0
proj_info['eccentricity'] = 0.081819190842621
proj_info['standard_parallel'] = 71.
proj_info['longitude_rot'] = 0.
proj_info['hemisphere'] = 'south'
# Offset of grid node centers. Lower left corner coordinates.
# Note sign change compared to matlab version!
proj_info['falseeasting'] = -3040000
proj_info['falsenorthing'] = -3040000

# Specify output angle type (degrees or radians)
output_data_type = 'degrees'

# Specify various ISM grids at different resolution
#rk = [32, 16, 8, 4, 2, 1]
#rk = [32]
#rk = [0.5]
rk = [3040] # upper limit

# grid dimensions of 1 km base grid
nx_base = 6081
ny_base = 6081

# choose which output file to write
flag_nc = True
flag_xy = True
flag_af2 = True


# CISM g1 grid where ice thickness and SMB are defined
grids1 = []
for r in rk:
    # For any resolution but check integer grid numbers
    nx = ((nx_base-1)/r)+1
    ny = ((ny_base-1)/r)+1
    if isaninteger(nx) and isaninteger(ny):
        agrid = {}
        agrid['dx'] = r*1000.
        agrid['dy'] = r*1000.
        agrid['nx'] = int(nx)
        agrid['ny'] = int(ny)
        agrid['offsetx'] = 0.
        agrid['offsety'] = 0.
        agrid['LatLonOutputFileName'] = 'grid_CISM3_g1_AIS_{:05d}m.nc'.format(int(r*1000))
        agrid['xyOutputFileName'] = 'xy_CISM3_g1_AIS_{:05d}m.nc'.format(int(r*1000))
        agrid['af2OutputFileName'] = 'af2_CISM3_g1_AIS_{:05d}m.nc'.format(int(r*1000))
        grids1.append(agrid)
    else:
        print('Warning: resolution {} km is not comensurable, skipped.'.format(r))

# Create grids and write out
for agrid in grids1:
    #print(agrid)
    success = generate_CDO_files(agrid, proj_info, output_data_type, flag_nc, flag_xy, flag_af2)


# CISM g0 grid where horizontal velocities are defined
grids0 = []
for r in rk:
    # For any resolution but check integer grid numbers
    nx = ((nx_base-1)/r)
    ny = ((ny_base-1)/r)
    if isaninteger(nx) and isaninteger(ny):
        agrid = {}
        agrid['dx'] = r*1000.
        agrid['dy'] = r*1000.
        agrid['nx'] = int(nx)
        agrid['ny'] = int(ny)
        agrid['offsetx'] = r*1000./2.
        agrid['offsety'] = r*1000./2.
        agrid['LatLonOutputFileName'] = 'grid_CISM3_g0_AIS_{:05d}m.nc'.format(int(r*1000))
        agrid['xyOutputFileName'] = 'xy_CISM3_g0_AIS_{:05d}m.nc'.format(int(r*1000))
        agrid['af2OutputFileName'] = 'af2_CISM3_g0_AIS_{:05d}m.nc'.format(int(r*1000))
        grids0.append(agrid)
    else:
        print('Warning: resolution {} km is not comensurable, skipped.'.format(r))

# Create grids and write out
for agrid in grids0:
    #print(agrid)
    success = generate_CDO_files(agrid, proj_info, output_data_type, flag_nc, flag_xy, flag_af2)
