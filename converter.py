# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 09:37:16 2025

@author: dcriggjp
"""

import math
import re

DEGREES_RE = re.compile('(\d+)°')
MINUTES_RE = re.compile(r"(\d+)'")
SECONDS_RE = re.compile('(\d+)"')

def radians_to_degrees(radians: float):
    return radians * 180/math.pi

def dd_to_dms(dd: float) -> tuple[float]:
    degree = math.trunc(dd)
    abs_dd = abs(dd)
    abs_d = abs(degree)
    
    minutes = math.trunc((abs_dd-abs_d)*60)
    
    seconds = (abs_dd-abs_d-minutes/60) * 3600
    return degree, minutes, seconds


def dms_to_dd(degrees: float, minutes: float, seconds: float) -> float:
    if degrees >= 0:
        dd = degrees + minutes/60 + seconds/3600
    else:
        dd = degrees - minutes/60 - seconds/3600
    return dd


def read_dms_str(dms_str: str) -> tuple[float]:
    degrees = float(DEGREES_RE.search(dms_str).group()[:-1])
    minutes = float(MINUTES_RE.search(dms_str).group()[:-1])
    seconds = float(SECONDS_RE.search(dms_str).group()[:-1])
    
    # Cardinal(?) direction
    card_direct = dms_str[-1]
    if (card_direct == 'W') or (card_direct == 'S'):
        degrees *= -1
    
    return (degrees, minutes, seconds)
