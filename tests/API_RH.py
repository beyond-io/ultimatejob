# Import and load necessary lib
from bs4 import BeautifulSoup
import requests


def extract_jobs_url(soup):
    jobs_links = []
    list_jobs_links = []
    jobs_list = soup.find("div", {"class": "container-fluid iCIMS_JobsTable"})
    jobs = jobs_list.find_all("a", {"class": "iCIMS_Anchor"})
    links = [link['href'] for link in jobs]
    jobs_links = links
    for link in jobs_links:
        list_jobs_links.append(link)
        # Need to push to a db
    print("-------URLs--------")
    print(list_jobs_links)
    return list_jobs_links


def extract_jobs_title(soup):
    jobs_titles = []
    list_jobs_titles = []
    jobs_list = soup.find("div", {"class": "container-fluid iCIMS_JobsTable"})
    jobs = jobs_list.find_all("a", {"class": "iCIMS_Anchor"})
    titles = [title['title'] for title in jobs]
    jobs_titles = titles
    for title in jobs_titles:
        list_jobs_titles.append(title)
        # Need to push to a db
    print("-------Titles--------")
    print(list_jobs_titles)
    return list_jobs_titles


def create_soup(req):
    soup = BeautifulSoup(req.content, 'html.parser')
    # print(soup.prettify())
    return soup


def check_status_code(req):
    print(req.status_code)
    return(req.status_code)


def create_req():
    # Load our first page
    # Need to pull from db
    search_url = "https://careers-redhat.icims.com/jobs/search?ss=1&in_iframe=1&searchLocation=13269--Raanana"
    req = requests.get(search_url)
    return req
