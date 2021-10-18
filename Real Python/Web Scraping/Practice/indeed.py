from bs4 import BeautifulSoup
import requests
url = "https://au.indeed.com/jobs?q=data%20engineer&l=Melbourne%20VIC"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
page_content = soup.find(id="mosaic-zone-jobcards")
slider_container = page_content.find_all('div', 'slider_container')
for slider in slider_container:
    job_table = slider.find('table')
    for job in job_table:
        position = job.find_all('h2')
        for span in position:
            span_title = span.find_all('span')
            if len(span_title) > 1:
                print(f'Position: {span_title[1].get_text()}')
            else:
                print(f'Position: {span_title[0].get_text()}')
        company_name = job.find('span', class_='companyName')
        location = job.find('div', class_='companyLocation')
        print(f'Company Name: {company_name.get_text()}')
        print(f'Location: {location.get_text()}')
