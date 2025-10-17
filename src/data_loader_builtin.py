"""
Data loader is responsible for loading travel times
between given stations from the XLSX file.
Author: Azeria 2025
"""

from typing import List
import pandas as pd

from connections import Connection

class DataLoader:
    """
    Utility class for loading data from the spreadsheet and creating connections
    """
    @staticmethod
    def load_connections(file: str) -> List[Connection]:
        """
        Load all connections from the spreadsheet

        Args:
            file (str): File to read

        Returns:
            List[Connection]: Returns a list of all the connections
        """
        # Load the connections from the spreadsheet
        data_frame: pd.DataFrame = pd.read_excel(file, engine='openpyxl', header=None)

        # Create the connections by iterating over the data frame
        network: List[Connection] = []
        for _, i in data_frame.iterrows():
            # Extract properties each entry contains
            line: str = i[0]
            start: str = i[1]

            # Check if the station was a termini or not
            end: str = i[2] if len(i) > 2 and pd.notna(i[2]) else None

            # Retrieve the travel time between the stations
            travel_time_str: str = i[3] if len(i) > 3 and pd.notna(i[3]) else None
            travel_time: int = 0

            # Validate travel time is a number
            if isinstance(travel_time_str, (int, float)):
                travel_time = int(travel_time_str)

            # Skip list of connections
            if end is None or travel_time is None:
                continue

            # Create and append the connection
            new: Connection = Connection(start=start, end=end, line=line, travel_time=travel_time)
            network.append(new)

        return network

if __name__ == "__main__":
    # Load the connections
    print("Creating connections from data frame")
    connections: List[Connection] = DataLoader.load_connections("../data/London Underground data.xlsx")

    # Display first ten connections
    print("First ten connections:")
    for connection in connections[:10]:
        print(f"- {connection}")
