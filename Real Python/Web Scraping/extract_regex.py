import re
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode('utf-8')

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", '', title)
# print(title)


# print(html)
string = "Name:"
start = html.find(string) + len(string)
end = html[start:]
end_index = end.find("<")
text_end = start + end_index
# print(html.find("<"))
his_name = html[start:text_end]
print(his_name)

color = html.find("Favorite Color:") + len("Favorite Color:")
wine = html[color:].find("<")
wine_end = color + wine
fave_color = html[color:wine_end]
# print(fave_color)
# print(html[start:])

# for string in ["Name:", "Favorite Color:"]:
#     string_start_idx = html.find(string)
#     text_start_idx = string_start_idx + len(string)

#     next_html_tag_offset = html[text_start_idx:].find("<")
#     text_end_idx = text_start_idx + next_html_tag_offset

#     raw_text = html[text_start_idx: text_end_idx]
#     clean_text = raw_text.strip(" \r\n\t")
#     print(clean_text)
