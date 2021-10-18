import mechanicalsoup
browser = mechanicalsoup.StatefulBrowser()
browser.open("http://olympus.realpython.org/login")
html_page = browser.page
browser.select_form()
browser.form.print_summary()
browser["user"] = "zeus"
browser["pwd"] = "ThunderDude"
response = browser.submit_selected()
print(browser.url)
