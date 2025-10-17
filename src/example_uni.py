"""
Example file using Built-in python list
Author: Azeria

Important:
The provided LinkedList does not provide append
so each item is prepended instead.
This means the items are the inverse order
in which they are listed in the spreadsheet
"""

from connections import Connection
from data_loader_uni import DataLoader


def main() -> None:
    """
    Load the connections
    """
    network: Connection = DataLoader.load_connections("../data/London Underground data.xlsx")

    # Display first ten connections
    print("First ten connections:")
    count: int = 0
    for connection in network.iterator():
        if count >= 10:
            break
        print(f"- {connection}")
        count += 1

if __name__ == "__main__":
    main()
