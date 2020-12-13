import pytest
from API_FB import Manipulation

def test_API_FB():
    """The testing will check if our functions return the required output"""
    expected_output_urls = [ https://www.facebook.com/careers/jobs/1672813472870915/, https://www.facebook.com/careers/jobs/712878282607325/, https://www.facebook.com/careers/jobs/420212419368641/, https://www.facebook.com/careers/jobs/207984144060781/, https://www.facebook.com/careers/jobs/773785633436218/, https://www.facebook.com/careers/jobs/2597607417128369/, https://www.facebook.com/careers/jobs/323705805605018/, https://www.facebook.com/careers/jobs/536078547072736/]
    assert Manipulation()==expected_output_urls,"The tests for URLs were successful"