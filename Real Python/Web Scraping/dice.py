import mechanicalsoup
import time
browser = mechanicalsoup.Browser()

for i in range(4):
    url = "http://olympus.realpython.org/dice"
    page_html = browser.get(url).soup
    # print(page_html)
    tag = page_html.select("#result")[0]
    result = tag.text
    print(f"The result of your dice roll is {result}")
    time.sleep(3)
