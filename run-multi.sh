#!/bin/bash

# Hawaii
#lonA=-165
#lonB=-145
#latA=10
#latB=30

# config2
#lonA=-150
#lonB=-110
#latA=-60
#latB=-20

# config3
lonA=20
lonB=107
latA=-10
latB=78

dlon=10
dlat=10
resolution=0.25

for lon0 in `seq $lonA $dlon $lonB`; do
    for lat0 in `seq $latA $dlat $latB`; do
	# echo $dlon $dlat
	(( lon1 = lon0 + dlon ))
	(( lat1 = lat0 + dlat ))
	bash /home/chaitra/Desktop/iospec_test/examples/netcdf/NOGGIN/run-vnp02.sh $lon0 $lat0 $lon1 $lat1 $resolution
    done
done
