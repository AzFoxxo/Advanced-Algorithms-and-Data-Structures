"""
Data class representing connections
Author: Azeria 2025
"""

from dataclasses import dataclass

@dataclass
class Connection:
    """
    Connection represents a connection between a two stations on a given line

    Attributes:
        line (str): Line name the connection is on.
        start (str): Starting station
        end (str): Next station along
        travel_time (int): Time in minutes between the stations
    """
    line: str
    start: str
    end: str
    travel_time: int

    # Override string representation
    def __str__(self) -> str:
        return f"{self.start} to {self.end} is {self.travel_time} minutes by the {self.line} line."
