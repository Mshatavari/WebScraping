import bs4
import requests

res = requests.get('https://en.wikipedia.org/wiki/Computing')
soup = bs4.BeautifulSoup(res.text, 'html.parser')
paragraphs = (soup.text)
count_0 = paragraphs.count('computing')
count_1 = paragraphs.count('Computing')
'''print(soup)'''
print(paragraphs)
print(count_0 + count_1)




