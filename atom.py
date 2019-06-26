import numpy
from constants import T, round


class Atom:
    def __init__(self, position=(0, 0, 0), mass=0, speed=0, acceleration=0, charge=0):
        self._position = numpy.array(position)
        self._mass = mass
        self._speed = speed
        self._acceleration = acceleration
        self._charge = charge

        self._d_position = dict()
        self._d_speed = dict()
        self._d_acceleration = dict()
        self._d_charge = dict()

        self.calculate(0)

    @property

    def calculate(self, t=None, r=None):
        r = round(t) if t is not None else r

        if r == 0:
            self._d_position[r] = self._position
            self._d_speed[r] = self._speed
            self._d_acceleration[r] = self._acceleration
            self._d_charge[r] = self._charge
        else:
            dv = 

            self._d_position[r] =


