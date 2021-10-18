import requests
from bs4 import BeautifulSoup
url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
result_container = soup.find(id="ResultsContainer")
job_elements = result_container.find_all("div", "card-content")
# for job_element in job_elements:
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print(title_element.text.strip())
#     print(company_element.text.strip())
#     print(location_element.text.strip())
#     print()
python_jobs = result_container.find_all(
    "h2", string=lambda text: "python" in text.lower())


python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs]

for python_job in python_job_elements:
    desired_job = python_job.find('h2', class_="title")
    # print(desired_job.text.strip())

for element in python_job_elements:
    links = element.find_all('a')[1]['href']
    print(f"Apply here: {links}")
    # for link in links:
    #     link_url = link['href']
    #     if link_url != "https://www.realpython.com":
    #         print(f"Apply here: {link_url}")
