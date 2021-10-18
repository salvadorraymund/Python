from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")


profile_list = soup.find_all("a")
profile_url = "http://olympus.realpython.org"
for profile in profile_list:
    greek_god = profile["href"]
    print(profile_url + greek_god)
