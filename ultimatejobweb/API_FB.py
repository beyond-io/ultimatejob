<<<<<<< HEAD
# Import and load necessary lib
import requests
from bs4 import BeautifulSoup as bs


class Manipulation:
=======
class Manipulation_FB:
>>>>>>> 7c51a51 (Update API_FB.py)
    def extract_jobs_list(self):
        fb_url = "https://www.facebook.com"
        jobs_links = []
        list_jobs_links = []
        jobs_list = self.find("div", {"class": "_8tk7"})
        jobs = jobs_list.find_all("a", {"class": "_8sef"})
        links = [link['href'] for link in jobs]
        jobs_links = links
        for link in jobs_links:
            list_jobs_links.append(fb_url+link)
            # Need to push to a db
        return list_jobs_links

    def extract_jobs_title(self):
        jobs_titles = []
        list_jobs_titles = []
        jobs_list = self.find("div", {"class": "_8tk7"})
        jobs = jobs_list.find_all("div", {"class": "_8sel"})
        jobs_titles = jobs
        for title in jobs_titles:
            list_jobs_titles.append(title.get_text())
            # Need to push to a db
        return list_jobs_titles
<<<<<<< HEAD


class main():
    # Load our first page
    search_url = "https://www.facebook.com/careers/jobs/?q="

    # Need to pull from db
    prefrences = "DevOps"
    r = requests.get(search_url+prefrences)

    # Checking if content is available
    # print(r.status_code)

    soup = bs(r.content, 'html.parser')
    # print(soup.prettify())

    Manipulation.extract_jobs_list(soup)

    Manipulation.extract_jobs_title(soup)

    pytest
=======
>>>>>>> 7c51a51 (Update API_FB.py)
