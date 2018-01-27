import math
from .position import Position

class DistanceCalculator(object):
    ''' This class would need to get the lat and long from a database and could
        be reused for more cities
    '''

    _EARTH_RADIUS = 6371  # Kms
    _DUBLIN_LAT = math.radians(53.339428)
    _DUBLIN_LONG = math.radians(-6.257664)

    @staticmethod
    def to_dublin(position):
        ''' Takes latitude and longitude in degrees and returns the distance in
            KMs to Dublin
        '''
        try:
            latitude, longitude = (math.radians(position.latitude),
                                   math.radians(position.longitude))

            central_angle = math.acos(math.sin(DistanceCalculator._DUBLIN_LAT) \
                * math.sin(latitude) \
                + math.cos(DistanceCalculator._DUBLIN_LAT) * math.cos(latitude) \
                * math.cos(math.fabs(DistanceCalculator._DUBLIN_LONG - longitude)))

            return DistanceCalculator._EARTH_RADIUS * central_angle
        except TypeError:
            return None
