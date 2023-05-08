import requests
from bs4 import BeautifulSoup
import pandas as pd

names = []
companys = []
phones = []
links = []
prices = []
for i in range(1, 113):
    page = requests.get('https://www.realtor.com/realestateagents/boston_ma/pg-'+str(i)) # Getting page HTML through request
    soup = BeautifulSoup(page.content, 'html.parser') # Parsing content using beautifulsoup
    s = soup.find('div', class_= 'cardWrapper')
    ui = s.find('ul', class_='jsx-1526930885')
    for divs in ui.find_all('div', class_='agent-list-card'):
        priceDiv = divs.find('div', class_='second-column')
        spans = priceDiv.find_all('span')
        if (len(spans) > 1):
            price = spans[0].text
            lower_str, upper_str = price.split("-")
            lower_str = lower_str.replace(" ", "")
            upper_str = upper_str.replace(" ", "")
            if(lower_str[-1]=="K"):
                a = float(lower_str[1:-1])/1000.0
            else:
                a = float(lower_str[1:-1])
            if(upper_str[-1]=="K"):
                b = float(upper_str[1:-1])/1000.0
            else:
                b = float(upper_str[1:-1])
            if a <= 2.0 <= b:
                phoneNumber = divs.find('div', class_='agent-phone')
                agentName = divs.find('div', class_="agent-list-card-title-text").find('a')
                companyNameDiv = divs.find('div', class_='agent-group')
                companyName = companyNameDiv.find('span')
                names.append(agentName.text)
                companys.append(companyName.text)
                if (phoneNumber):
                    phones.append(phoneNumber.text)
                else:
                    phones.append("none")
                links.append('realtor.com' + agentName.get('href'))
                prices.append(price)            
        else:
            price = "none"
df = pd.DataFrame({'agent_name':names,'agent_phone':phones,'company_name':companys,'realtor_link':links, 'activity_range':prices})
df.to_csv('high.csv', index=False, encoding='utf-8')