## ✈️ FlightMemory Scraper
A Python project that scrapes flight history from [FlightMemory.com](https://www.flightmemory.com/) and cleans the data into a structured format for analysis.

### 📁 Project Structure
* flightmemory.py — Scrapes flight data and saves it as a CSV.
* flightcleaner.py — Cleans and processes the raw CSV data (dates, times, durations).
* flightdata.py — Defines a FlightData enum for standardized column names and table indexes.
* session.py — Handles login and HTTP session management using requests.Session.
* flights.csv — The raw scraped data (ignored in .gitignore if sensitive).
* user.json — Contains login credentials (not tracked in Git for safety).
