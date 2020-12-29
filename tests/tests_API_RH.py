# Import and load necessary lib
# import sys
# sys.path.append('vagrant\ultimatejob')
import API_FB
import API_RH


# Test functions
def test_api_urls():
    """The testing will check if our functions return the required output"""
    # Create soup object & print a status message - 404 not good , 200 good
    soup = API_RH.create_soup(API_RH.create_req())
    expected_output_urls = ['https://global-redhat.icims.com/jobs/80964/senior-devops-engineer---telco-5g-integration/job?hub=7&in_iframe=1',
                            'https://global-redhat.icims.com/jobs/83546/senior-product-security-engineer---devsecops-managed-services/job?hub=7&in_iframe=1',
                            'https://global-redhat.icims.com/jobs/83285/ci-and-devops-internship/job?hub=7&in_iframe=1',
                            'https://global-redhat.icims.com/jobs/69711/software-quality-engineering-internship---local-student-position/job?hub=7&in_iframe=1',
                            'https://global-redhat.icims.com/jobs/81168/software-quality-engineer---storage-red-hat-virtualization/job?hub=7&in_iframe=1',
                            'https://global-redhat.icims.com/jobs/70227/talent-acquisition-recruiter%2c-engineering-team---12-month-contract/job?hub=7&in_iframe=1',
                            'https://global-redhat.icims.com/jobs/83236/principal-software-engineer---object-and-data-services-%28noobaa%29/job?hub=7&in_iframe=1',
                            'https://global-redhat.icims.com/jobs/82632/sales-renewals/job?hub=7&in_iframe=1',
                            'https://global-redhat.icims.com/jobs/81944/senior-technical-writer/job?hub=7&in_iframe=1',
                            'https://global-redhat.icims.com/jobs/77210/software-quality-engineer---openshift-deployment/job?hub=7&in_iframe=1']
    assert API_RH.extract_jobs_url(soup) == expected_output_urls, "The tests for URLs were successful"


def test_api_titles():
    # Create soup object & print a status message - 404 not good , 200 good
    soup = API_RH.create_soup(API_RH.create_req())
    """The testing will check if our functions return the required output"""
    expected_output_titles = ['\nJob Title\n\nSenior DevOps Engineer - TelCo 5G Integration',
                            '\nJob Title\n\nSenior Product Security Engineer - DevSecOps Managed Services',
                            '\nJob Title\n\nCI and DevOps Internship',
                            '\nJob Title\n\nSoftware Quality Engineering Internship - Local Student Position',
                            '\nJob Title\n\nSoftware Quality Engineer - Storage Red Hat Virtualization',
                            '\nJob Title\n\nTalent Acquisition Recruiter, Engineering Team - 12 month contract',
                            '\nJob Title\n\nPrincipal Software Engineer - Object and Data Services (NooBaa)',
                            '\nJob Title\n\nSales Renewals', '\nJob Title\n\nSenior Technical Writer',
                            '\nJob Title\n\nSoftware Quality Engineer - OpenShift Deployment']
    assert API_RH.extract_jobs_title(soup) == expected_output_titles, "The tests for URLs were successful"
