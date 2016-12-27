#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 11:06:51 2016

@author: lukas
"""
import numpy as np
import matplotlib.pyplot as pl
import numpy.polynomial.polynomial as poly

number_of_points = 50

lineStyles = {':': '_draw_dotted', '--': '_draw_dashed', '-.': '_draw_dash_dot', '-': '_draw_solid'}
line_styles_list = list(lineStyles.keys())

## case parallel
edge_length = 1

volume_cube =  edge_length**3

diago_cube = np.sqrt(3)*edge_length
distance_to_surface = np.linspace((diago_cube/2),0,number_of_points)

side_a_bottom_cube = edge_length - (edge_length/2) - distance_to_surface 
side_b_bottom_cube = edge_length
side_c_bottom_cube = edge_length
volume_bottom_cube = side_a_bottom_cube * side_b_bottom_cube * side_c_bottom_cube

right_contribution_case2_3d = (volume_cube - volume_bottom_cube) / volume_cube
right_contribution_case2_3d[right_contribution_case2_3d >= 1] = 1

wrong_contribution_case2_3d = 1 - right_contribution_case2_3d

fig2 = pl.figure()
ax2 = fig2.add_subplot(111)

ax2.plot(distance_to_surface, right_contribution_case2_3d, linestyle=line_styles_list[1] , color=str(0/10) ,linewidth=2.0, label='parallel')

# case rotated
vertex_angle_bottom_triangle_rad = np.deg2rad(45)
height_bottom_prism = diago_cube - diago_cube/2 - distance_to_surface
    
base_length_bottom_pyramid = (2*height_bottom_prism)*np.tan(vertex_angle_bottom_triangle_rad/2)

volume_bottom_prism = 0.5 *  height_bottom_prism * base_length_bottom_pyramid * edge_length

right_contribution_case1_3d = (volume_cube - volume_bottom_prism)/volume_cube
wrong_contribution_case1_3d = 1 - right_contribution_case1_3d

ax2.plot(distance_to_surface, right_contribution_case1_3d,  linestyle=line_styles_list[3] , color=str(1/10), linewidth=2.0, label='rotated')

mean_contribution = (right_contribution_case1_3d + right_contribution_case2_3d) / 2

ax2.plot(distance_to_surface, mean_contribution,  linestyle=line_styles_list[2] , linewidth=2.0,color=str(2/10), label='mean')

# polynomial fit
# http://stackoverflow.com/questions/19165259/python-numpy-scipy-curve-fitting

# calculate polynomial
z = np.polyfit(distance_to_surface, mean_contribution, 3)
f = np.poly1d(z)

# calculate new x's and y's
y_new = f(distance_to_surface)

ax2.plot(distance_to_surface, y_new,color=str(2/10) , linestyle=line_styles_list[0], linewidth=2.0, label='polyfit mean')
pl.xlabel('distance to surface')
pl.ylabel('right_contribution')
pl.grid(True)
pl.legend(loc='lower right')

# test case parallel aligned voxel with distance = 0.25 and edge length = 1 -> right contribution = 0.75
test_distance = 0.5
assert_weight_factor = f(test_distance)