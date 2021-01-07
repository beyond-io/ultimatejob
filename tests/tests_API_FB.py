# Import and load necessary lib
import API_FB


# Test functions
def test_api_urls():
    """The testing will check if our functions return the required output"""
    # Test the status message - 404 not good , 200 good
    assert API_FB.create_req().status_code == 200, "The tests for URLs were successful"
