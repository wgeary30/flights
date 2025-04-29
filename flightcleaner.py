"""
William Geary
Flights
29 April 2025
--------------------------------------------------------------------------------
flightcleaner
"""

# Import modules
import numpy as np
import pandas as pd

from datetime import datetime, timedelta
from flightdata import FlightData

# FlightCleaner class
class FlightCleaner():

    def __init__(self, df):
        self.df_orig = df
        self.df = df

    def clean_dates(self):
        """ Clean flightdata departure and arrival dates """
        self.df["dep_date"] = pd.to_datetime(self.df[FlightData.DATE.header],
            format="%m-%d-%Y", errors="coerce"
        ).dt.date

        self.df["arr_date"] = np.where(
            self.df[FlightData.ARR_TIME.header].str.contains("\\+1", na=False),
            self.df["dep_date"] + timedelta(days=1),
            self.df["dep_date"]
        )
        return self

    def clean_time_column(self, col, fmt="%I:%M %p"):
        """ Clean time column given a certain format """
        self.df[col] = pd.to_datetime(self.df[col], format=fmt, errors="coerce").dt.time
        return self

    def clean_times(self):
        """ Clean flightdata departure and arrival times """
        self.clean_time_column(FlightData.DEP_TIME.header)

        self.df[FlightData.ARR_TIME.header] = self.df[FlightData.ARR_TIME.header].apply(
            lambda x: x.replace("+1", "").strip() if isinstance(x, str) else x
        )
        self.clean_time_column(FlightData.ARR_TIME.header)
        return self

    def combine_date_time(self, date_col, time_col, new_col):
        """ Combine a date and time to create a new column """
        self.df[new_col] = self.df.apply(
            lambda row: datetime.combine(row[date_col], row[time_col])
            if pd.notnull(row[date_col]) and pd.notnull(row[time_col]) else pd.NaT,
            axis=1
        )
        return self

    def clean_distance(self):
        """ Remove text, convert the data type for distance """
        self.df[FlightData.DISTANCE.header] = self.df[FlightData.DISTANCE.header].apply(
            lambda x: int(x.split()[0].replace(",", ""))
        )
        return self

    def clean_duration(self):
        """ Convert the flight duration into minutes """
        self.df[FlightData.DURATION.header] =  self.df[FlightData.DURATION.header].apply(lambda x:
            (int(x.split(":")[0])) * 60 + int(x.split(":")[1].replace("h", "").strip()))
        return self

    def clean_seat_info(self):
        """ Clean the seat information into two columns """
        self.df["seat_num"] = self.df[FlightData.SEAT.header].apply(lambda x: x.split("/")[0])
        self.df["seat_loc"] = self.df[FlightData.SEAT.header].apply(lambda x: x.split("/")[1])
        return self

    def get_cleaned_df(self):
        """ Get the current, cleaned flightdata dataframe"""
        return self.df