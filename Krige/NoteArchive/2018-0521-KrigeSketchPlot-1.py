#!/usr/bin/env python
"""
Plot data from a selected tile.
"""

import json
import math
import os
import sys
from time import gmtime, strftime

import noggin
import MODIS_DataField as mdf

# from MODIS_DataField import MODIS_DataField, BoundingBox, mdf.Point, box_covering, Polygon, data_src_directory

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

from scipy.spatial import ConvexHull

_plot_source_data_inside_grid  = True
_plot_source_data_outside_grid = True
_plot_source_data_sampled      = True
_plot_kriged                   = True
_plot_kriged_results           = True
_plot_kriged_outline           = True
_plot_kriged_data_index        = True

gridz       = _capture_z      
gridss      = _capture_ss
gridx       = _capture_x      
gridy       = _capture_y      
data1       = _capture_data1  
longitude1  = _capture_x1     
latitude1   = _capture_y1     
ex_grid     = _capture_ex_grid
in_grid     = _capture_in_grid
kr          = _capture_kr
k           = _capture_k
data_x      = _capture_data_x
data_y      = _capture_data_y
data_z      = _capture_data_z

krige_results = [kr]

marker_size = 3.5
m_alpha = 1.0
colormap_0 = plt.cm.rainbow
colormap_1 = plt.cm.gist_yarg
colormap_2 = plt.cm.plasma
colormap_x = colormap_0
# vmin=1.0; vmax=5.0
vmin=-2.0; vmax=1.25
# vmin=np.nanmin(data1); vmax=np.nanmax(data1)

if True:
    print strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    print 'plot results'
    #### PLOT RESULTS ####
    #
    # fig = plt.gcf()
    fig_gen = noggin.fig_generator(1,1)
    fig,ax = plt.subplots(1,1)
    _scale = 2.0*np.pi
    wh_scale = [_scale,_scale]
    # lon_0,lat_0 = kr.box.centroid().inDegrees()
    lon_0,lat_0 = (0,0)
    # m = Basemap(projection='laea', resolution='l', lat_ts=65\
    ##     #            ,width=wh_scale[0]*3000000,height=wh_scale[1]*2500000)
    m = Basemap(projection='cyl',resolution='h'\
                ,ax=ax\
                ,lat_0=lat_0, lon_0=lon_0)
    m.drawcoastlines(linewidth=0.5)
    m.drawparallels(np.arange(-90., 91., 10.), labels=[1, 0, 0, 0])
    m.drawmeridians(np.arange(-180, 181., 30), labels=[0, 0, 0, 1])
    m.drawmapboundary(fill_color='dimgrey')
    
    if _plot_source_data_outside_grid:
        modis_obj_2 = mdf.MODIS_DataField(\
                                          data=np.log10(data1[ex_grid]+1.0e-9)\
                                          ,latitude=latitude1[ex_grid]\
                                          ,longitude=longitude1[ex_grid])
        modis_obj_2.scatterplot(m=m\
                                ,title='scatter'\
                                ,plt_show = False\
                                ,vmin=vmin,vmax=vmax\
                                ,cmap=colormap_x)

    if _plot_source_data_inside_grid:
        modis_obj_3 = mdf.MODIS_DataField(\
                                          data=np.log10(data1[in_grid]+1.0e-9)\
                                          ,latitude=latitude1[in_grid]\
                                          ,longitude=longitude1[in_grid])
        modis_obj_3.scatterplot(m=m\
                                ,title='scatter'\
                                ,plt_show = False\
                                ,vmin=vmin,vmax=vmax\
                                ,cmap=colormap_x)
    if _plot_kriged:
        for kr in krige_results:
            if _plot_kriged_results:
                # m = modis_obj_2.get_m()
                # m.scatter(kr.x,kr.y,c=kr.z\
                    # m.scatter(gridx,gridy,c=gridz\
                    m.scatter(gridx,gridy,c=np.log10(gridz+1.0e-9)\
                              ,cmap=colormap_x\
                              ,linewidth=0\
                              ,alpha=m_alpha\
                              ,latlon=True\
                              ,vmin=vmin, vmax=vmax\
                              ,edgecolors=None\
                              ,s=marker_size*10\
                              ,marker='s'\
                    )
            if _plot_kriged_outline:
                noggin\
                    .draw_screen_poly( kr.x[kr.hull.vertices]\
                                       ,kr.y[kr.hull.vertices]\
                                       ,m\
                                       ,edgecolor='white' )
            if _plot_kriged_data_index:
                # xt, yt = m( np.sum(kr.x)/kr.x.size, np.sum(kr.y)/kr.y.size )
                xt, yt = m( np.nanmin(kr.x), np.sum(kr.y)/kr.y.size )
                # if xt < 0.0:
                #     xt = xt+360.0
                # xt, yt = ( np.sum(kr.x)/kr.x.size, np.sum(kr.y)/kr.y.size )
                plt.text(xt,yt,str(k),color='green')

            if _plot_source_data_sampled:
                m.scatter(data_x,data_y, s=marker_size, cmap=colormap_x,
                          edgecolors=(0.0,1.0,0.0),
                          linewidth=1,
                          alpha=m_alpha*0.5,
                          latlon=True,
                          vmin=vmin, vmax=vmax,
                          facecolors='none'
                )
                
                
print strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
if True:
    print 'plt.show'
    plt.show()

print strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
print 'KrigeSketch done'
