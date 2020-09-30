from abc import ABC, abstractmethod

class Measurement():

    def __init__(self, name, unit):
        self._name = name
        self._unit = unit
        self.value = -1000.0


    def get(self):
        return "{0}={1:4.2f} {2}".format(self._name, self.value, self._unit)

class Device(ABC):

    @abstractmethod
    def get_measurements(self):
        """Get all possible measurements"""