# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:
    """base class"""
    def __init__(self):
        pass

class FlightVehicle(Vehicle):
    """child of Vehicle"""
    def __init__(self):
        pass

# Following the diagram, Starship looks like it should be a child
# of Vehicle. Changed to pass unittest 

# class Starship(Vehicle):
#     """child of Vehicle"""
#     def __init__(self):
#         pass

class Starship(FlightVehicle):
    def __init__(self):
        pass

class GroundVehicle(Vehicle):
    """child of Vehicle"""
    def __init__(self):
        pass

class Car(GroundVehicle):
    """child of Ground Vehicle"""
    def __init__(self):
        pass

class Motorcycle(GroundVehicle):
    """child of Ground Vehicle"""
    def __init__(self):
        pass

class Airplane(FlightVehicle):
    """child of Flight Vehicle"""
    def __init__(self):
        pass