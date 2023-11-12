import requests
from bs4 import BeautifulSoup

custom_headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9'
}

def scrape_amazon_product_link(product_name):
    base_url = "https://www.amazon.ca/s?k="
    search_url = base_url + product_name.replace(" ", "+")

    print(search_url)
    response = requests.get(search_url, headers=custom_headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the first link that matches the pattern
        for link in soup.find_all('a', href=True):
            if "/dp/" in link['href']:
                # Check if the link matches the desired pattern
                if link['href'].startswith("https://www.amazon.ca/") and "/dp/" in link['href']:
                    # Extract the product link
                    product_link = link['href']

                    # Print or store the link as needed
                    print(f"Found product link: {product_link}")

                    # You can save the entire product link to a variable or return it as needed
                    return product_link

    else:
        print(f"Error: {response.status_code}")

    return None

# Example usage:
product_name_to_search = "Coca-Cola Coke Classic, 355mL Cans, Pack of 12"
product_link = scrape_amazon_product_link(product_name_to_search)

