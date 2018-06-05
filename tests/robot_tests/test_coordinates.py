import unittest

from numpy import testing
from numpy import deg2rad

from robot.coordinates import make_coords


class TestCoordinates(unittest.TestCase):

    def test_transform(self):
        coord = make_coords()
        coord.transform(make_coords(pos=[1, 2, 3]))
        testing.assert_array_equal(coord.pos,
                                   [1, 2, 3])

    def test_transformation(self):
        c = make_coords(rot=[deg2rad(10), 0, 0])
        d = make_coords(rot=[deg2rad(20), 0, 0])
        testing.assert_almost_equal(
            c.transformation(d).worldrot(),
            make_coords(rot=[deg2rad(10), 0, 0]).worldrot())