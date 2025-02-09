# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 09:28:23 2025

@author: dcriggjp
"""

from coordinate import Coordinate, calc_coordinate_distance, calc_coordinate_bearing


lat_1_str = '31°37\'54"S'
long_1_str =  '68°27\'15"W'



home_lat = 43.6026259
home_long = -116.1889928

work_lat = 43.6102716
work_long = -116.1974092

from soverflow import distance
d = distance(home_lat, home_long, work_lat, work_long)*1000

home = Coordinate(home_lat, home_long)
work = Coordinate(work_lat, work_long)


c_d = calc_coordinate_distance(home, work)
c_d2 = calc_coordinate_distance(work, home)

k_home = Coordinate.from_dms_str('43°29\'02.3"N', '116°25\'26.3"W')


jk_bearing = calc_coordinate_bearing(k_home, home)
jk_distance = calc_coordinate_distance(k_home, home)


