import requests
from bs4 import BeautifulSoup
def virtualvocations_script(search):
    url='https://www.virtualvocations.com/jobs/q-'+search+'/c-100%25+remote'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    jobs=soup.find_all("li", class_="card mb-3 job-card")


    virtualvocationsjobs={}




    for job in jobs:



        job_link=job.find("a")

        job_title = job_link['title']
        job_url=job_link['href']

        job_age=job.find("small",class_="text-black-20 my-1")


        job_description=job.find("p",class_="job-excerpt mt-3 mb-0")
        virtualvocationsjobs[job_title.strip()]={'title':job_title.strip(),'url':job_url,'age':job_age.text.strip().replace('Posted ',''),'description':job_description.text.strip()}


    return virtualvocationsjobs


