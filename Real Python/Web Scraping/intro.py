from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode('utf-8')
# print(html)

title_index = html.find("<title>")
# print(title_index)
start_index = title_index + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
# print(title)

url2 = "http://olympus.realpython.org/profiles/poseidon"
page2 = urlopen(url2)
html_bytes2 = page2.read()
html2 = html_bytes2.decode('utf-8')
# print(html2)
start = html2.find("<title>") + len("<title>")
end = html2.find("</title>")
title2 = html2[start:end]
print(html_bytes2)
