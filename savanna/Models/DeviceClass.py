from enum import Enum, unique, auto

"""
A risk based classification system for all medical devices ((Federal Food, Drug, and Cosmetic Act, section 513)
"""
@unique
class Classification(Enum):
    """
    Class I (low to moderate risk): general controls
    """
    Class1 = auto()
    """
    Class II (moderate to high risk): general controls and special controls
    """
    Class2 = auto()
    """
    Class III (high risk): general controls and Premarket Approval (PMA)
    """
    Class3 = auto()
    """
    Unclassified
    """
    U = auto()
    """
    Not classified
    """
    N = auto()
    """
    HDE
    """
    F = auto()