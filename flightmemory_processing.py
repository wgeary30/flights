"""
William Geary
Flights
29 April 2025
--------------------------------------------------------------------------------
flightmemory_procesing
"""

# Import modules
import pandas as pd

from flightcleaner import FlightCleaner
from flightdata import FlightData

# Constants
FLIGHTS_FILE = "flights.csv"

def main():

    # Read the flights file
    flights = pd.read_csv(FLIGHTS_FILE)

    # Clean the departure and arrival dates and times
    cleaner = (
        FlightCleaner(flights)
        .clean_dates()
        .clean_times()
        .combine_date_time("dep_date", FlightData.DEP_TIME.header, "departure")
        .combine_date_time("arr_date",  FlightData.ARR_TIME.header, "arrival")
        .clean_distance()
        .clean_duration()
        .clean_seat_info()
    )

    # Get the new, cleaned flightdata
    cleaned_df = cleaner.get_cleaned_df()

    # Return all flightdata
    cleaned_df.to_csv("flights_processed.csv", index=False)
    print(f"Complete - {cleaned_df.shape[0]} rows, {cleaned_df.shape[1]} columns")

if __name__ == "__main__":
    main()