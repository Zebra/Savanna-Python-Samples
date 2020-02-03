from enum import Enum

"""
Rotation --- Describes image orientation.

@author Dbuhrsmith@zebra.com

"""

class Rotation(Enum):
    Normal = "N"
    Clockwise = "R"
    Inverted = "I"
    Counterclockwise = "L"

    def get(self):
        return self.value