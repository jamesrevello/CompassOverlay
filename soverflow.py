# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 09:18:04 2025

The answer I got from StackOverflow:
https://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula#answer-21623206

@author: dcriggjp
"""

from math import sin, cos, asin, atan, sqrt, pi

from converter import radians_to_degrees

def distance(lat1, lon1, lat2, lon2):
    r = 6371 # km
    p = pi / 180

    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return 2 * r * asin(sqrt(a))


def angle_from_lat_longs(lat1, lon1, lat2, lon2):
    dlon = lon1-lon2
    
    y = sin(dlon)*cos(lat2)
    x = cos(lat1) * sin(lat2) - sin(lat1)*cos(lat2)*cos(dlon)
    
    # Bearing
    brng = radians_to_degrees(atan(y/x))
    brng = (brng + 360) % 360
    # I dont think this works
    # brng = 360 - brng # 
    return brng
    