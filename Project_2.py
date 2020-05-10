import bs4
import requests
import re
import webbrowser

res = requests.get('https://en.wikipedia.org/wiki/Computing')
soup = bs4.BeautifulSoup(res.text, 'html.parser')
paragraphs = (soup.text)
def count_computing():
    count_0 = paragraphs.count('computing')
    count_1 = paragraphs.count('Computing')
    sum = (count_0 + count_1)
    return sum
print("Total words of computing on a Wikipedia page = ", count_computing())

my_list = []
for link in soup.findAll('a', duplicates = False):
    my_list.append(link.get('href'))
'''my_list = str(my_list)
my_list.sort()'''
print(my_list)
print(len(my_list))

'''incompleted_list = []
pathfind_3 = re.compile('\w+\S+')
pathfind_4 = re.search(pathfind_3, my_list)
print(pathfind_4.group())
pathfind_4 = re.findall(pathfind_3, my_list)
for j in pathfind_4:
    incompleted_list.append(j)
print(incompleted_list)
print(len(incompleted_list))'''

'''a = []
b = [x for x in my_list if x not in incompleted_list]
a.append(b)
print(a)'''

'''string= (u'#) character save as string
for i:len(mylist)
 if string == myslist(i,1:4)
  mylist.delete(i)
          end
          end

list_complete = []
list_incomplete = []
for urls in range(len(my_list)):
    if my_list(urls).startswith("http"):
        list_complete.append(my_list(urls))
        print(len(list_complete))'''


'''url = 'https://en.wikipedia.org/wiki/'
for data in my_list:
    webbrowser.open_new_tab(url + 'data/')
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    paragraphs = (soup.text)'''
    
'''for urls in links:
    urls.get("https://en.wikipedia.org/wiki/Computation")
    urls.click()
    count_computing()
        
my_list = []
for link in soup.findAll('a'):
    my_list.append(link.get('href'))
my_list = str(my_list)
print(my_list)'''


'''with open("p2.txt", "w") as f:
    f.write(my_list)    
f.close()'''
