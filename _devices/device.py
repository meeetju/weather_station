from abc import ABC, abstractmethod
from collections import namedtuple


class Measurement():

    def __init__(self, name, unit):
        self._name = name
        self._unit = unit
        self.value = -1000.0

    @property
    def name(self):
        return self._name

    @property
    def unit(self):
        return self._unit

    def __str__(self):
        return "{0}={1:4.2f} {2}".format(self._name, self.value, self._unit)

class Device(ABC):

    @abstractmethod
    def get_measurements(self):
        """Get all possible measurements"""