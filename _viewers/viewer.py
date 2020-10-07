from abc import ABC, abstractmethod


class Viewer(ABC):

    @abstractmethod
    def update_view(self):
        """Update view with data"""
