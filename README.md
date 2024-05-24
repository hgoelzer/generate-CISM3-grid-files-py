# generate-CISM3-grid-files-py
Python scripts to generate grid description files used for cdo regridding for CISM3

## Setup
Needs a python3 environment with  
numpy, netCDF4, os

The scripts can generate 3 different types of files for Greenland and Antarctica

### grid description files (needed for CDO regridding)
  grid_CISM3_g?_<IS>_<res>.nc
### xy coordinates 
  xy_CISM3_g?_<IS>_<res>.nc
### area factors 
  af2_CISM3_g?_<IS>_<res>.nc

All files are produced for the grids g1 (ice thickness, SMB, ..) and g0 (horizontal velocities)
  CISM3_AIS_multigrid_generater_nc.py  
  CISM3_GrIS_multigrid_generater_nc.py  

using  

  polar_stereo.py  
  wnc.py  
