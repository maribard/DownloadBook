import os
import bs4
import requests
import urllib.request
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


def download_file(download_url, filename):
    response = urllib.request.urlopen(download_url)    
    path = 'C:\VS Code Programs\DownloadBook\saved'
    completeName = os.path.join(path, filename + ".pdf") 
    file = open(completeName, 'wb')
    file.write(response.read())
    file.close()



def download_book(param_href):


        driver = webdriver.Chrome('C:/Users/m.bardyn/AppData/Local/Temp/Temp1_chromedriver_win32.zip/chromedriver.exe')
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.set_page_load_timeout(50)
        driver.get('https://www.salesmanago.com/')
        

        driver.find_element_by_link_text('resources').click()
        driver.find_element_by_link_text('Ebooks').click()
        driver.find_element_by_xpath('//a[@href="{}"]'.format(param_href)).click()
        driver.switch_to.window(driver.window_handles[1])


        dates_for_4_inputs = ['Mariusz Bardyn', 'mariusz.bardyn.benhauer+testrekrutacja@salesmanago.com ', 'SpaceX', 'spacex.com']
        textboxes = driver.find_elements_by_class_name('form-control')

        count = 0
        for value in textboxes:
                if count == 4:
                        break
                # enter value
                value.send_keys(dates_for_4_inputs[count])
                # increment count value
                count += 1

        grade_dropdown = Select(textboxes[4])
        grade_dropdown.select_by_index(167)
        textboxes[6].send_keys("796390840")


        response_my = requests.get(param_href)
        soup2 = bs4.BeautifulSoup(response_my.text,"lxml")
        title_text = soup2.select('.btn')
        

        old_title = title_text[0].getText()
        new_title = "".join(line.strip() for line in old_title.split("\n"))
        

        if new_title == "Download eBook":
                driver.find_element_by_class_name('chevron-container').click()
                time.sleep(1)
                driver.find_element_by_link_text('Download ebook').click()
                time.sleep(1)

                driver.switch_to.window(driver.window_handles[2])
                download_file(driver.current_url, "Ebook")
                time.sleep(1)

        else:
                driver.switch_to.frame(driver.find_element_by_xpath('/html/body/div[3]/div/div/iframe[2]'))
                driver.find_element_by_xpath('/html/body/div/div').click()
                driver.switch_to.window(driver.window_handles[1])

                driver.find_element_by_class_name('chevron-container').click()
                time.sleep(2)
                driver.find_element_by_link_text('HERE').click()
                time.sleep(3)

                driver.switch_to.window(driver.window_handles[2])
                print(driver.current_url)
                download_file(driver.current_url, "Ebook")
                

        time.sleep(2)

        driver.quit()

        if os.path.exists('C:\VS Code Programs\DownloadBook\saved\Ebook.pdf'):
                return True
        else:
                return False
        
       


