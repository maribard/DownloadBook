from downloading import download_book
from selenium import webdriver
import requests
import bs4
import lxml


def download_book_with_name(name_of_book):
    dict_map_url_to_title = create_dict_map_url_to_title()
    for key, value in dict_map_url_to_title.items():
        if name_of_book in key or key in name_of_book:
            wanted_url = value
            result = download_book(wanted_url)
    
    return result




def create_dict_map_url_to_title():


    list_of_title = []
    dict_map_url_to_title = dict()


    res = requests.get("https://www.salesmanago.com/info/knowledgecenter.htm")
    soup = bs4.BeautifulSoup(res.text,"lxml")
    title_tag = soup.select('.ebook__img--container a')


    for a in title_tag:
        my_url = a['href']

        res2 = requests.get(my_url)
        soup2 = bs4.BeautifulSoup(res2.text,"lxml")
        title_text = soup2.select('.ebook__title')



        if len(title_text) > 0:
            old_title = title_text[0].getText()
            new_title = "".join(line.strip() for line in old_title.split("\n"))
            dict_map_url_to_title[new_title] = my_url
            list_of_title.append(new_title)
        else:
            title_text = soup2.select('.register-form__headline')
            old_title = title_text[0].getText()
            new_title = "".join(line.strip() for line in old_title.split("\n"))
            dict_map_url_to_title[new_title] = my_url
            list_of_title.append(new_title)


    return dict_map_url_to_title


wanted_book = "Internet of Things for marketers"
wanted_book2 = "Online Consumer Trends 2020"






