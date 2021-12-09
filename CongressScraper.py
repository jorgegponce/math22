import requests
from bs4 import BeautifulSoup

main = requests.get("https://www.congress.gov/sponsors-cosponsors/116th-congress/senators/all")

soup = BeautifulSoup(main.content, 'html.parser')
#print(soup.prettify())
main_table = soup.find(class_="table-wrapper")

#print(main_table.prettify())
senator_names = []
senator_names_links = []

senator_dict = {}
senators_dicts = {}

for senator in main_table.find_all('tr'):
    #print(senator.prettify())
    for name in senator.find_all('td', {"data-text": True}):
        senator_dict = {}
        senator_names.append(name.get_text())
        senator_dict.update({'name':name.get_text()})
        senator_names_links.append("https://www.congress.gov"+ name.find("a")['href'])
        senator_dict.update({'law':"https://www.congress.gov"+ name.find("a")['href']})
        senators_dicts.update({name.get_text():senator_dict})

#print(senator_names_links)
#print(len(senator_names_links))

branch_senator = requests.get(senator_names_links[10]+'?q=%7B"bill-status"%3A"law"%7D')

senator_soup = BeautifulSoup(branch_senator.content, 'html.parser')

#print(senator_soup.prettify())

senator_bill_table = senator_soup.find_all('ol', class_="basic-search-results-lists expanded-view")

senator_bills = []

for bills in senator_bill_table:
    #rint(bills.get_text())
    for bill in bills.find_all('li', class_="expanded"):
        #print(bill.get_text())
        senator_bills.append("https://www.congress.gov"+bill.find('span', class_="result-heading").find('a')['href'])

#print(len(senator_bill_table))

print(senator_bills[0])

print(senators_dicts[senator_names[0]]['law'])



