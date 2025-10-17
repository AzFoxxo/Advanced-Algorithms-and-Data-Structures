"""
Example file using Built-in python list
Author: Azeria

Important:
Appends each node in order unlike LinkedList example.
"""

from connections import Connection
from data_loader_builtin import DataLoader

def main() -> None:
    """
    Load the connections
    """
    network: Connection = DataLoader.load_connections("../data/London Underground data.xlsx")

    # Display first ten connections
    print("First ten connections:")
    for connection in network[:10]:
        print(f"- {connection}")

if __name__ == "__main__":
    main()
