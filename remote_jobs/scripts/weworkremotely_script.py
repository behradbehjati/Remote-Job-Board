import requests
from bs4 import BeautifulSoup
def weworkremotely_script(search):
    url='https://weworkremotely.com/remote-jobs/search?term='+search+'&button=&sort=any_time'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    jobs=soup.find_all("li", class_="feature")

    weworkremotelyjobs={}




    for job in jobs:

        job_title=job.find("span",class_="title")

        job_link=job.find_all("a")
        job_url='https://weworkremotely.com/'+job_link[1]['href']

        #job_age=job.find("div",class_="job-age")
        job_description=job.find("span",class_="region company")
        weworkremotelyjobs[job_title.text.strip()]={'title':job_title.text.strip(),'url':job_url,'description':job_description.text.strip(),'age':''}


    return weworkremotelyjobs

