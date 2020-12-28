# Import and load necessary lib
# import sys
# sys.path.append('vagrant\ultimatejob')
import API_FB


# Test functions
def test_api_urls():
    """The testing will check if our functions return the required output"""
    # Create soup object & print a status message - 404 not good , 200 good
    soup = API_FB.create_soup(API_FB.create_req())
    expected_output_urls = ['https://www.facebook.com/careers/v2/jobs/1035151026857199/',
                            'https://www.facebook.com/careers/v2/jobs/271572833959882/',
                            'https://www.facebook.com/careers/v2/jobs/2744793102315021/',
                            'https://www.facebook.com/careers/v2/jobs/413395136285498/',
                            'https://www.facebook.com/careers/v2/jobs/241312920567692/',
                            'https://www.facebook.com/careers/v2/jobs/2348482432126226/',
                            'https://www.facebook.com/careers/v2/jobs/2771660556270346/',
                            'https://www.facebook.com/careers/v2/jobs/1240872639590159/',
                            'https://www.facebook.com/careers/v2/jobs/366294361177202/',
                            'https://www.facebook.com/careers/v2/jobs/534731380508736/',
                            'https://www.facebook.com/careers/v2/jobs/259439192068027/',
                            'https://www.facebook.com/careers/v2/jobs/669051024038731/',
                            'https://www.facebook.com/careers/v2/jobs/668617893843325/',
                            'https://www.facebook.com/careers/v2/jobs/3303081543132838/',
                            'https://www.facebook.com/careers/v2/jobs/335620370840567/',
                            'https://www.facebook.com/careers/v2/jobs/1664419727065261/',
                            'https://www.facebook.com/careers/v2/jobs/1531612870338560/',
                            'https://www.facebook.com/careers/v2/jobs/701347943948255/',
                            'https://www.facebook.com/careers/v2/jobs/1016867915398698/',
                            'https://www.facebook.com/careers/v2/jobs/638369416899968/',
                            'https://www.facebook.com/careers/v2/jobs/3457874277626614/',
                            'https://www.facebook.com/careers/v2/jobs/277880939889661/',
                            'https://www.facebook.com/careers/v2/jobs/3353944101321143/',
                            'https://www.facebook.com/careers/v2/jobs/525027894909915/',
                            'https://www.facebook.com/careers/v2/jobs/711702592764107/']
    assert API_FB.extract_jobs_url(soup) == expected_output_urls, "The tests for URLs were successful"


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
                                'Controls Operations Program Manager',
                                'Critical Facility Engineer',
                                'Manager, Production Engineering',
                                'Research Intern, Integrated Circuit Design (PhD)',
                                'Data Scientist Manager, Fraud',
                                'Product Manager, Research Platform ',
                                'Software Engineer, AI (EMEA)',
                                'Client Solutions Manager, Philippines']
    assert API_FB.extract_jobs_title(soup) == expected_output_titles, "The tests for URLs were successful"
