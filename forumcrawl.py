from bs4 import BeautifulSoup
import requests
urla = "*CHANGE TO THREAD PAGE*"
landing = requests.get(urla)
tomatosoup = BeautifulSoup(landing.text, 'lxml')
page = tomatosoup.find('li', class_='pageNav-page')
finalpage = page.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text

url='*CHANGE TO THREAD PAGE*' + finalpage

f = requests.get(url)
soup = BeautifulSoup(f.text, 'lxml')
for match in soup.find_all('div', class_='bbWrapper'):
    content = match.text
    cleancontent = content.replace('Click to expand...', '').replace('said:\n\n', 'said:').replace('\n\n', '\n').strip('\n')
    print(cleancontent)
    print("-------------------------------")


