from bs4 import BeautifulSoup
import requests
custom_headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9'
}




url = 'https://www.amazon.ca/dp/B000VA1CWO/ref=cm_gf_aatv_iaac_d_p0_e0_qd0_U6XXxeTRejV2QRN4c40i?th=1'

response = requests.get(url, headers= custom_headers)
soup = BeautifulSoup(response.content, 'html.parser')
itemLabels = soup.find_all(class_="a-color-secondary a-size-base prodDetSectionEntry")
itemDetails = soup.find_all(class_='a-size-base prodDetAttrValue')
productName = soup.find(id="productTitle")


x = 0
print(productName.text.strip())
for label in itemLabels:
    print(label.text.strip(), itemDetails[x].text.strip())
    x += 1
# for itemLabel in itemLabels:
#     if "Item Weight" in itemLabel.text.strip():
#         print(itemLabel.text.strip())  

#         for itemDetail in itemDetails:
#             if 'Kilograms' in itemDetail.text.strip():
#                 # print(itemDetail.text.strip())  
#                 itemWeight = itemDetail.text.strip()
#                 print(itemWeight)
#         break

