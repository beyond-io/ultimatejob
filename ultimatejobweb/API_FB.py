class Manipulation_FB:
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
