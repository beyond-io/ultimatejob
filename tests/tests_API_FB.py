# Import and load necessary lib
# import sys
# sys.path.append('vagrant\ultimatejob')
import API_FB


# Test functions
def test_api_urls():
    """The testing will check if our functions return the required output"""
    # Test the status message - 404 not good , 200 good
    assert API_FB.check_status_code(API_FB.create_req()) == 200, "The tests for URLs were successful"


def test_api_titles():
    # Create soup object & print a status message - 404 not good , 200 good
    soup = API_FB.create_soup(API_FB.create_req())
    """The testing will check if our functions return the required output"""
    expected_output_titles = ['Engineering Manager - Malware Analysis Infrastructure',
                              'Software Engineer, Android',
                              'Software Engineer, Machine Learning',
                              'Manager, Software Engineering (AR Commerce)',
                              'Android Software Engineer',
                              'Industrial Design Architect - FRL',
                              'Software Engineer, Vision',
                              'Battery System Engineer',
                              'Product Designer, Portal Product Lines',
                              'Software Engineer, AI (EMEA)',
                              'Instructional Design Lead',
                              'Research Scientist, Vision',
                              'Web Manager, Facebook for Business',
                              'Infrastructure Network Engineer',
                              'Enterprise Technical Support Analyst, Workplace',
                              'Director of Human Resources, Technology EMEA',
                              'Data Protection Associate General Counsel',
                              'Manager, Production Engineering',
                              'Research Intern, Integrated Circuit Design (PhD)',
                              'Data Scientist Manager, Fraud',
                              'Product Manager, Research Platform ',
                              'Software Engineer, AI (EMEA)',
                              'Client Solutions Manager, Philippines',
                              'Hardware Systems Engineer, Compute',
                              'Production Engineer']
    assert API_FB.extract_jobs_title(soup) == expected_output_titles, "The tests for URLs were successful"
