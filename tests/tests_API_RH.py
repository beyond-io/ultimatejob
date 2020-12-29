# Import and load necessary lib
# import sys
# sys.path.append('vagrant\ultimatejob')
import API_RH


# Test functions
def test_api_urls():
    """The testing will check if our functions return the required output"""
    # Create soup object & print a status message - 404 not good , 200 good
    soup = API_RH.create_soup(API_RH.create_req())
    expected_output_urls = ['https://global-redhat.icims.com/jobs/69710/software-development-internship---red-hat-virtualization%2c-student-position/job?hub=7&in_iframe=1',
                            'https://global-redhat.icims.com/jobs/80964/senior-devops-engineer---telco-5g-integration/job?hub=7&in_iframe=1',
                            'https://global-redhat.icims.com/jobs/83546/senior-product-security-engineer---devsecops-managed-services/job?hub=7&in_iframe=1',
                            'https://global-redhat.icims.com/jobs/83285/ci-and-devops-internship/job?hub=7&in_iframe=1',
                            'https://global-redhat.icims.com/jobs/69711/software-quality-engineering-internship---local-student-position/job?hub=7&in_iframe=1',
                            'https://global-redhat.icims.com/jobs/81168/software-quality-engineer---storage-red-hat-virtualization/job?hub=7&in_iframe=1',
                            'https://global-redhat.icims.com/jobs/70227/talent-acquisition-recruiter%2c-engineering-team---12-month-contract/job?hub=7&in_iframe=1',
                            'https://global-redhat.icims.com/jobs/83236/principal-software-engineer---object-and-data-services-%28noobaa%29/job?hub=7&in_iframe=1',
                            'https://global-redhat.icims.com/jobs/82632/sales-renewals-representative/job?hub=7&in_iframe=1',
                            'https://global-redhat.icims.com/jobs/81944/senior-technical-writer/job?hub=7&in_iframe=1']
    assert API_RH.extract_jobs_url(soup) == expected_output_urls, "The tests for URLs were successful"


def test_api_titles():
    # Create soup object & print a status message - 404 not good , 200 good
    soup = API_RH.create_soup(API_RH.create_req())
    """The testing will check if our functions return the required output"""
    expected_output_titles = ['69710 - Software Development Internship - Red Hat Virtualization, Student Position',
                              '80964 - Senior DevOps Engineer - TelCo 5G Integration',
                              '83546 - Senior Product Security Engineer - DevSecOps Managed Services',
                              '83285 - CI and DevOps Internship',
                              '69711 - Software Quality Engineering Internship - Local Student Position',
                              '81168 - Software Quality Engineer - Storage Red Hat Virtualization',
                              '70227 - Talent Acquisition Recruiter, Engineering Team - 12 month contract',
                              '83236 - Principal Software Engineer - Object and Data Services (NooBaa)',
                              '82632 - Sales Renewals Representative', '81944 - Senior Technical Writer']
    assert API_RH.extract_jobs_title(soup) == expected_output_titles, "The tests for URLs were successful"
