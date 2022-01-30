import struct
from turtle import width

width, height = struct.unpack('<HH', gif[6:10])
width, height