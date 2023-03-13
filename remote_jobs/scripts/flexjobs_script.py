import requests
from bs4 import BeautifulSoup
def flexjobs_script(search):
    url='https://www.flexjobs.com/search?categories_unpacked=true&search='+search+'&tele_level%5B%5D=All+Telecommuting&location='
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    jobs=soup.find_all("li", class_="m-0 row job")
    flexjobs={}




    for job in jobs:

        job_title=job.find("a",class_="job-title job-link")
        job_url='https://www.flexjobs.com'+job_title['href']
        job_age=job.find("div",class_="job-age")
        job_description=job.find("div",class_="job-description")
        flexjobs[job_title.text.strip()]={'title':job_title.text.strip(),'url':job_url,'age':job_age.text.strip(),'description':job_description.text.strip()}


    return flexjobs

