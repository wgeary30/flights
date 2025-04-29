"""
William Geary
Flights
28 April 2025
--------------------------------------------------------------------------------
flightdata
"""

# Import modules
from enum import Enum

# FlightData class
class FlightData(Enum):

    NUM = ("num", "td", 0, 0)
    DATE = ("date", "td", 1, 0)
    DEP_TIME = ("dep_time", "td", 1, 1)
    ARR_TIME = ("arr_time", "td", 1, 2)
    DEP_IATA = ("dep_iata", "td", 2, 0)
    DEP_CITY = ("dep_city", "td", 3, 0)
    DEP_COUNTRY = ("dep_country", "td", 3, 1)
    DEP_NAME = ("dep_name", "td", 3, 2)
    ARR_IATA = ("arr_iata", "td", 4, 0)
    ARR_CITY = ("arr_city", "td", 5, 0)
    ARR_COUNTRY = ("arr_country", "td", 5, 1)
    ARR_NAME = ("arr_name", "td", 5, 2)
    DISTANCE = ("distance", "th", 0, [0, 1])
    DURATION = ("duration", "th", 0, [2, 3])
    AIRLINE = ("airline", "td", 6, 0)
    FLIGHT_NUM = ("flight_num", "td", 6, 1)
    AIRCRAFT = ("aircraft", "td", 7, 0)
    AIRCRAFT_REGISTRATION = ("aircraft_registration", "td", 7, 1)
    AIRCRAFT_NAME = ("aircraft_name", "td", 7, 2)
    SEAT = ("seat", "td", 8, 0)
    TRAVEL_CLASS = ("travel_class", "td", 8, 1)
    FLIGHT_AS = ("flight_as", "td", 8, 2)
    FLIGHT_REASON = ("flight_reason","td", 8, 3)

    # Properties
    @property
    def header(self):
        return self.value[0]

    @property
    def tag(self):
        return self.value[1]

    @property
    def index(self):
        return self.value[2]

    @property
    def secondary_index(self):
        return self.value[3]