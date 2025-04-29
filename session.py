"""
William Geary
Flights
28 April 2025
--------------------------------------------------------------------------------
session
"""

# Import modules
import requests
from bs4 import BeautifulSoup

# Session class
class Session:

    def __init__(self, root=None):
        self.root = root
        self.session = requests.Session()

    def __str__(self):
        return f"Session ({self.root})"

    def get_session(self):
        """ Get the current session """
        return self.session

    def get(self, url, **kwargs):
        """ Get request """
        response = self.session.get(url, params=kwargs)
        return self._response_handling(response)

    def post(self, url, **kwargs):
        """ Post request """
        response = self.session.post(url, data=kwargs)
        return self._response_handling(response)

    def login(self, login_url, **kwargs):
        """ Login to session if required """
        response = self.post(login_url, **kwargs)
        return self._response_handling(response)

    def close(self):
        """ Close the session """
        self.session.close()
        print(f"{self} closed")

    @staticmethod
    def parse_response(response):
        """ Parse the content of a html response """
        bs_response = BeautifulSoup(response.content, "html.parser")
        return bs_response

    # Internal methods
    @staticmethod
    def _response_handling(response):
        """ Response handling for errors """
        if response.status_code == 200:
            return response
        else:
            raise Exception(f"Login error ({response.status_code}): {response.reason}")