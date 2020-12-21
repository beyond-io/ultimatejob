# Import and load necessary lib
from API_FB import Manipulation_FB


class main():
    # Create soup object & print a status message - 404 not good , 200 good
    soup = Manipulation_FB.create_soup(Manipulation_FB.create_req())

    # Return list contains URLs
    Manipulation_FB.extract_jobs_url(soup)

    # Return list contains job titles
    Manipulation_FB.extract_jobs_title(soup)

    # Running the tests
    # pytest
