from abc import ABC, abstractmethod


class Viewer(ABC):

    @abstractmethod
    def update_view(self, *args,  **kwargs):
        """Update view with data"""
