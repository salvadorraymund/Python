from bs4 import BeautifulSoup
import requests

url = "https://pythonjobs.github.io/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
job_list = soup.find(class_='job_list')
jobs = job_list.find_all('div', class_='job')
for job in jobs:
    job_title = job.find('h1')
    link = job.find('a').get('href')
    info = job.find_all('span', string=lambda text: 'i-globe')
    print(f'Position available: {job_title.text.strip()}')
    print(f'Location: {info[0].text.strip()}')
    print(f'Posting Date: {info[1].text.strip()}')
    print(f'Tenure: {info[2].text.strip()}')
    print(f'Company: {info[3].text.strip()}')
    print(f'Apply here: https:/{link}')
    print()

# job_info = job_list.find_all(class_='info')
# # print(job_info)
# # job_info = job_list.find_all('span', class_='info')
# # print(job_info)
# for job in jobs:
    
    
