from bs4 import BeautifulSoup
import requests
import pandas as pd


#Function to extract product name
def get_product_name(soup):
    try:
        product_name = soup.find('h1',attrs={'id':'testProName'}).text

    except AttributeError:
        product_name = ""

    return product_name


#Function to extract selling price of the product
def get_selling_price(soup):
    try:
        price = soup.find('span',attrs={'class':'sellingPrice mr-1'}).text

    except AttributeError:
        price = ""

    return price



#Function to extract the MRP of the product
def get_mrp(soup):
    try:
        mrp = soup.find('div',attrs={'class':'discPrice mr-2'}).text

    except AttributeError:
        mrp = ""

    return mrp



#Function to extract the discount% of the product
def get_discount(soup):
    try:
        discount = soup.find('div',attrs={'class':'offers offer-perc-o'}).text

    except AttributeError:
        discount = ""

    return discount



if __name__ == '__main__':

    #webpage url
    url = 'https://www.bewakoof.com/custom-tshirts?gender=men'

    #http request
    webpage = requests.get(url)

    soup = BeautifulSoup(webpage.content, 'html.parser')

    links = soup.find_all('a',attrs={'class':'col-sm-4 col-xs-6 px-2'})

    links_list = []

    for link in links:
        links_list.append(link.get('href'))

    d = {"Product Name":[], "Selling Price":[], "MRP":[], "Discount":[]}

    #Loop for extracting details
    for link in links_list:
        new_webpage = requests.get("https://www.bewakoof.com" + link)
        new_soup = BeautifulSoup(new_webpage.content, 'html.parser')

        d['Product Name'].append(get_product_name(new_soup))
        d['Selling Price'].append(get_selling_price(new_soup))
        d['MRP'].append(get_mrp(new_soup))
        d['Discount'].append(get_discount(new_soup))


    bewakoof_df = pd.DataFrame.from_dict(d)
