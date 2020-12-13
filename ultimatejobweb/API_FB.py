# Import and load necessary lib
import requests
from bs4 import BeautifulSoup as bs

class Manipulation:
    def extract_jobs_list(self):
        fb_url = "https://www.facebook.com"
        jobs_links = []
        jobs_list = self.find("div", {"class": "_8tk7"})
        jobs = jobs_list.find_all("a", {"class": "_8sef"})
        links = [link['href'] for link in jobs]
        jobs_links = links
        for link in jobs_links:
            print(fb_url+link)
            # Need to push to a db


    def extract_jobs_title(self):
        jobs_titles = []
        jobs_list = self.find("div", {"class": "_8tk7"})
        jobs = jobs_list.find_all("div", {"class": "_8sel"})
        jobs_titles = jobs
        for title in jobs_titles:
            print(title.get_text())
            # Need to push to a db


class main():
    # Load our first page
    search_url = "https://www.facebook.com/careers/jobs/?q="

    # Need to pull from db
    prefrences = "DevOps"
    r = requests.get(search_url+prefrences)

    # Checking if content is available
    # print(r.status_code)

    soup = bs(r.content)
    # print(soup.prettify())


    Manipulation.extract_jobs_list(soup)


    Manipulation.extract_jobs_title(soup)