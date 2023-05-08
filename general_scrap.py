import requests
from bs4 import BeautifulSoup
import pandas as pd

names = []
companys = []
phones = []
links = []
for i in range(1, 113):
    page = requests.get('https://www.realtor.com/realestateagents/boston_ma/pg-'+str(i)) # Getting page HTML through request
    soup = BeautifulSoup(page.content, 'html.parser') # Parsing content using beautifulsoup
    s = soup.find('div', class_= 'cardWrapper')
    ui = s.find('ul', class_='jsx-1526930885')
    for a in ui.find_all('div', class_='agent-list-card-title-text'):
        phoneNumber = a.find('div', class_='agent-phone')
        agentName = a.find('a')
        companyNameDiv = a.find('div', class_='agent-group')
        companyName = companyNameDiv.find('span')
        names.append(agentName.text)
        companys.append(companyName.text)
        if (phoneNumber):
            phones.append(phoneNumber.text)
        else:
            phones.append("none")
        links.append('realtor.com' + agentName.get('href'))
df = pd.DataFrame({'agent_name':names,'agent_phone':phones,'company_name':companys,'realtor_link':links})
df.to_csv('data.csv', index=False, encoding='utf-8')