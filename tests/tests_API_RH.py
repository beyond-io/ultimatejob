# Import and load necessary lib
# import sys
# sys.path.append('vagrant\ultimatejob')
import API_RH


# Test functions
def test_api_urls():
    """The testing will check if our functions return the required output"""
    # Test the status message - 404 not good , 200 good
    assert API_RH.create_req().status_code == 200, "The tests for URLs were successful"


def test_api_titles():
    # Create soup object & print a status message - 404 not good , 200 good
    soup = API_RH.create_soup(API_RH.create_req())
    """The testing will check if our functions return the required output"""
    expected_output_titles = ['83236 - Principal Software Engineer - Object and Data Services (NooBaa)',
                              '83687 - Senior Software Quality Engineer - OpenShift Virtualization',
                              '83683 - Software Quality Engineer - Red Hat Virtualization',
                              '83651 - Delivery People Manager - Consulting Services',
                              '83660 - Quality Software Engineer Internship - Data Analyst',
                              '77210 - Software Quality Engineer - OpenShift Deployment',
                              '81943 - Software Engineer - Kubernetes Management',
                              '80964 - Senior DevOps Engineer - TelCo 5G Integration',
                              '83546 - Senior Product Security Engineer - DevSecOps Managed Services',
                              '70227 - Talent Acquisition Recruiter, Engineering Team - 12 month contract']
    assert API_RH.extract_jobs_title(soup) == expected_output_titles, "The tests for URLs were successful"
