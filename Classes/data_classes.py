from dataclasses import dataclass, field
from math import asin, cos, radians, sin, sqrt
from dataclasses import fields


@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

    def distance_to(self, other):
        """Calculate one position from another using the Haversine formula"""
        r = 6371
        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi1, phi2 = radians(self.lat), radians(other.lat)
        h = (sin((phi2 - phi1) / 2)**2
             + cos(phi1) * cos(phi2) * sin((lam_2 - lam_1) / 2)**2)
        return 2 * r * asin(sqrt(h))


@dataclass
class Capital(Position):
    country: str = 'Unknown'


Oslo = Position('Oslo', 10.8, 10.9)
Vancouver = Position('Vancouver', -123.1, 49.3)
oslo_to_vancouver = Oslo.distance_to(Vancouver)
# Oslo.name = "pos"
print(f"{Oslo.name} is located at {Oslo.lat}N and {Oslo.lon}E.")
print(f'The distance between Oslo and Vancouver is {oslo_to_vancouver}.')
# lat_unit = fields(Position)[2].metadata['unit']
# print(lat_unit)
Capital('Oslo', 10.8, 59.9, 'Norway')
