"""
William Geary
Flights
28 April 2025
--------------------------------------------------------------------------------
flightmemory
"""

# Import modules
import json
import pandas as pd
import re

from collections import defaultdict
from flightdata import FlightData
from session import Session

# Constants
ROOT = "https://www.flightmemory.com/"
LOGIN_URL = "https://www.flightmemory.com/signin/"
LANDING_URL = "https://www.flightmemory.com/signin/?go=check"
USER_JSON = "user.json"


def parse_user(user_json, username_key="username", password_key="password"):
    """ Parse the user json for username and password """
    with open(user_json, "r") as file:
        user = json.load(file)
        return user[username_key], user[password_key]


def get_table(bs_page, **kwargs):
    """ Get the table of flight data on a certain page """
    return bs_page.find("table", kwargs)


def get_value(row, field):
    """ Get the value from a cell given the field """

    # Find the cell and list of text values within
    cell = row.find_all(field.tag, recursive=False)[field.index]
    text_list = list(cell.stripped_strings)

    # Handle list splicing of secondary index
    if isinstance(field.secondary_index, list):
        value_list = text_list[field.secondary_index[0]:field.secondary_index[1] + 1]
        return " ".join(value_list)

    # Handle missing values
    if len(text_list) < field.secondary_index + 1:
        return None

    return text_list[field.secondary_index]


def get_flights(bs_page):
    """ Get a dataframe of the flights data on each page """

    # Get the table object, find its rows
    table = get_table(bs_page, cellspacing="2")
    rows = table.find_all("tr", {"valign" : "top"})
    flightdata = defaultdict(list)

    # Iterate through all flightdata rows on the page
    for row in rows:

        # Iterate through all fields in the flightdata table
        for field in FlightData:

            # Get the value from the field in the row
            value = get_value(row, field)

            # Add the value to the data dictionary, create a dataframe
            flightdata[field.header].append(value)

    return pd.DataFrame.from_dict(flightdata)


def next_page(bs_flightdata):
    """ Get the next page of flightdata if it exists """
    img_tag = bs_flightdata.find("img", {"src" : "/images/next.gif"})
    next_url = img_tag.find_parent("a").get("href") if img_tag else None

    return next_url


def get_dbpos(next_url):
    """ Get the dbpos value given the next url """
    dbpos = re.search("dbpos=(\\d+)", next_url)
    return dbpos.group(1) if dbpos else None


def main():

    # Create a new session, get user values
    s = Session(ROOT)
    user, password = parse_user(USER_JSON)

    try:

        # Login and open landing page
        s.login(LOGIN_URL, username=user, passwort=password, go="login")
        landing = s.get(LANDING_URL, go="check")
        bs_landing = s.parse_response(landing)

        # Find the "FLIGHTDATA" tab and URL
        flightdata_href = str(bs_landing.find("a", string="FLIGHTDATA").get("href"))
        flightdata_url = LOGIN_URL + flightdata_href

        # Open the "FLIGHTDATA" page
        flightdata = s.get(flightdata_url, go=flightdata_href)
        bs_flightdata = s.parse_response(flightdata)

        # Iterate through all pages of flightdata
        df = get_flights(bs_flightdata)

        while True:

            # Determine if a next page exists, and if so, its URL
            next_url = next_page(bs_flightdata)

            if next_url:
                # Get the parameters to pass when getting next flightdata
                flightdata_url = LOGIN_URL + str(next_url)
                dbpos = get_dbpos(next_url)

                # Parse the next page of flightdata
                flightdata = s.get(flightdata_url, go="flugdaten", dbpos=dbpos)
                bs_flightdata = s.parse_response(flightdata)
                df = pd.concat([df, get_flights(bs_flightdata)])
            else:
                # Return all flightdata
                df.to_csv("flights.csv", index=False)
                print(f"Complete - {df.shape[0]} rows, {df.shape[1]} columns")

                break

    finally:
        s.close()


if __name__ == "__main__":
    main()