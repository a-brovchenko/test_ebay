import requests
from bs4 import BeautifulSoup as bs
import json


class EbayData:
    """
    A simple class for getting product data from the eBay website 
    """

    def __init__(self, product_id: int) -> None:
        self.url = f"https://www.ebay.com/itm/{product_id}"
        self.response = requests.get(self.url).text
        self.soup = bs(self.response, "lxml")


    def __get_price_product(self) -> str:
        self.price = self.soup.find('div', class_='vim x-price-section mar-t-20')
        self.price = self.price.find('span', class_='ux-textspans').text
        return self.price
    

    def __get_saller_name(self) -> str:
        self.saller_name = self.soup.find('div', class_='x-sellercard-atf__info__about-seller').get('title')
        return self.saller_name
    

    def __get_product_name(self) -> str:
        self.product_name = self.soup.find('h1', class_="x-item-title__mainTitle").text.strip()
        return self.product_name
    

    def __get_img_urls(self) -> list:
        self.photo = self.soup.find('div', class_='ux-image-grid-container filmstrip filmstrip-x')
        self.photo = self.photo.find_all('img')
        self.img_urls = [img['src'] if 'src' in img.attrs else img['data-src'] for img in self.photo]
        return self.img_urls


    def get_product_data(self) -> None:
        self.data = {
            "product_name": self.__get_product_name(),
            "product_price": self.__get_price_product(),
            "product_url": self.url,
            "saller_name": self.__get_saller_name(),
            "img_url": self.__get_img_urls()
        }
        print(json.dumps(self.data, indent=2))


if __name__ == "__main__":  
    product = EbayData(186522312139) # enter eBay item number here
    product.get_product_data()