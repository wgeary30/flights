"""
William Geary
Flights
29 April 2025
--------------------------------------------------------------------------------
aircraft
"""

# Import modules
from enum import Enum

# Aircraft class
class Aircraft(Enum):

    AIRBUS = ("Airbus", "airbus ([0-9]{3})", "Airbus _")  # Airbus a319, Airbus a321N, Airbus a330-200
    ATR = ("ATR", "atr ([0-9]+)", "ATR _")  # ATR-72-600
    BOEING = ("Boeing", "boeing ([0-9]{3})", "Boeing _")  # Boeing 737 MAX 8, Boeing 777-300
    BOMBARDIER = ("Bombardier", "bombardier crj-([0-9]{3})", "Bombardier CRJ-_")  # Bombardier CRJ-700
    CESSNA = ("Cessna", "cessna ([0-9]+)", "Cessna _")  # Cessna 172
    DHC = ("De Havilland Canada", "dhc-([0-9])", "DHC-_")  # DHC-8-400
    EMBRAER = ("Embraer", "embraer erj-([0-9]{3})", "Embraer ERJ-_")  # Embraer ERJ-190
    GULFSTREAM = ("Gulfstream", "gulfstream ([a-z0-9]+)", "Gulfstream _")  # Gulfstream G500, Gulfstream V

    @property
    def manufacturer(self):
        return self.value[0]

    @property
    def regex_rule(self):
        return self.value[1]

    @property
    def format(self):
        return self.value[2]