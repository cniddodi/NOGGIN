#!/bin/bash

# Example of Kriging L2 data onto a grid
#
# Data from https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level2/OMO3PR.003/2021/
#
# Note we interact with files as HDF5 not HDF5-EOS. This just means we interact with the
# data structures at a lower level.
#

#
export PYTHONPATH=/home/mrilee/git/NOGGIN-PyKrige:/Users/mrilee/git/NOGGIN
export NOGGIN_DATA_SRC_DIRECTORY=/home/mrilee/data/VIIRS

# Execute the calculation. Krige to a default 1-degree lon-lat grid.
#
# CLI Options
# -d <source data directory>
# -n <variable to extract>  # Note the low-level style of access via HDF-5
# -m <variogram functional model>
# -v # Verbose output
#
python ~/git/NOGGIN/Krige/noggin_krige.py \
       -f src_file_list \
       -d ${NOGGIN_DATA_SRC_DIRECTORY}/ \
       -n observation_data/l04 \
       -m gamma_rayleigh_nuggetless_variogram_model \
       -R -b 15 -35 30 -20 \
       -S 1000 \
       -v

# Gapfill on a grid
# python ~/git/NOGGIN/Krige/noggin_krige.py -d ${NOGGIN_DATA_SRC_DIRECTORY}/ -n Atmospheric_Water_Vapor_Mean -m gamma_rayleigh_nuggetless_variogram_model -v -G

