# Import and load necessary lib
import pytest
from API_FB import Manipulation_FB
import requests
from bs4 import BeautifulSoup as bs


class main():
    # Load our first page
    search_url = "https://www.facebook.com/careers/jobs/?q="

    # Need to pull from db
    prefrences = "DevOps"
    r = requests.get(search_url+prefrences)

    # Checking if content is available
    # print(r.status_code)

    soup = bs(r.content, 'html.parser')
    # print(soup.prettify())

    Manipulation_FB.extract_jobs_list(soup)

    Manipulation_FB.extract_jobs_title(soup)

    # Running the tests
    pytest
