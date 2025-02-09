# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 14:43:57 2025

@author: dcriggjp
"""

from converter import dd_to_dms, dms_to_dd, read_dms_str
from soverflow import distance, angle_from_lat_longs

# Decimal Degrees
class DD:
    def __init__(self, coordinate: float):
        self.coordinate = coordinate
    
    def __str__(self) -> str:
        return f'{self.coordinate}°'
    
    def __repr__(self) -> str:
        return f'{self.coordinate}'
    
    def to_dms(self):
        return DMS(*dd_to_dms(self.coordinate))



# Degrees Minutes Seconds
class DMS:
    def __init__(self, degrees: float, minutes: float, seconds: float):
        self.degrees = degrees
        self.minutes = minutes
        self.seconds = seconds
        
    def __str__(self) -> str:
        return f'{self.degrees}°{self.minutes}\'{self.seconds}"'
    
    # TODO I dont know what kind of things are useful for repr
    def __repr__(self) -> str:
        return self.__str__()
    
    @classmethod
    def from_dd(cls, dd: float):
        return cls(*dd_to_dms(dd))
    
    @classmethod
    def from_str(cls, dms_str: str):
        return cls(*read_dms_str(dms_str))
    
    def to_dd(self) -> float:
        return DD(dms_to_dd(self.degrees, self.minutes, self.seconds))


class Coordinate:
    def __init__(self, lat: float, long: float):
        self.lat = lat
        self.long = long
        
    @classmethod
    def from_dms(cls, northing: DMS, easting: DMS):
        # TODO These might be backwards
        lat = dms_to_dd(northing.degrees, northing.minutes, northing.seconds)
        long = dms_to_dd(easting.degrees, easting.minutes, easting.seconds)
        return cls(lat, long)
    
    @classmethod
    def from_dms_str(cls, northing: str, easting: str):
        lat = DMS.from_str(northing).to_dd().coordinate
        long = DMS.from_str(easting).to_dd().coordinate
        return cls(lat, long)
    
    def __str__(self) -> str:
        return f'({self.lat}, {self.long})'
    
    def __repr__(self) -> str:
        return self.__str__()

def calc_coordinate_distance(
        coordinate_1: Coordinate, 
        coordinate_2: Coordinate) -> float:
    dist = distance(
        coordinate_1.lat,
        coordinate_1.long,
        coordinate_2.lat,
        coordinate_2.long,
        )
    return dist

def calc_coordinate_bearing(
        coordinate_1: Coordinate, 
        coordinate_2: Coordinate) -> float:
    angle = angle_from_lat_longs(
        coordinate_1.lat, 
        coordinate_1.long, 
        coordinate_2.lat, 
        coordinate_2.long,
        )
    return angle
    