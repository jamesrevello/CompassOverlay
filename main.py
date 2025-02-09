# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 09:05:58 2025

@author: dcriggjp
"""

import coordinate as coor


work = coor.Coordinate.from_dms_str('43°36\'36"N', '116°11\'50"W')

rev = coor.Coordinate(43.7243869, -116.6408839)


distance = coor.calc_coordinate_distance(work, rev)
bearing = coor.calc_coordinate_bearing(work, rev)