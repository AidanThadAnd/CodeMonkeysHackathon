from bs4 import BeautifulSoup
import requests
custom_headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9'
}

url = 'https://www.amazon.com/Bose-QuietComfort-45-Bluetooth-Canceling-Headphones/dp/B098FKXT8L'

response = requests.get(url, headers= custom_headers)
soup = BeautifulSoup(response.content, 'html.parser')
itemLabels = soup.find_all(class_="a-color-secondary a-size-base prodDetSectionEntry")
itemDetails = soup.find_all(class_='a-size-base prodDetAttrValue')
itemWeight = None 

for itemLabel in itemLabels:
    if "Item Weight" in itemLabel.text.strip():
        print(itemLabel.text.strip())  

        for itemDetail in itemDetails:
            if 'Kilograms' in itemDetail.text.strip():
                # print(itemDetail.text.strip())  
                itemWeight = itemDetail.text.strip()
                print(itemWeight)
        break