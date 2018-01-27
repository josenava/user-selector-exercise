import unittest
from src.distance_calculator import DistanceCalculator
from src.position import Position

class DistanceCalculatorTest(unittest.TestCase):
    def test_wrong_type_coordinates_returns_none_as_distance(self):
        position_none = Position(None, None)
        position_str = Position("5.320", "-3.22")
        
        self.assertIsNone(DistanceCalculator.to_dublin(position_none))
        self.assertIsNone(DistanceCalculator.to_dublin(position_str))
    

if __name__ == '__main__':
    unittest.main()
