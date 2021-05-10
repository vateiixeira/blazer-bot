from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from csv import writer
from datetime import datetime
from selenium.common import exceptions
from selenium.common.exceptions import NoSuchElementException

LOCATION_CHROME_DRIVER_WINDOWS = 'C:\chromedriver_win32\chromedriver.exe'
LOCATION_CHROME_DRIVER_LINUX ='/home/vinicius/dev/chromedriver_linux64/chromedriver'

class Blazer:
    def __init__(self):        
        #chorme_options.add_argument("--headless")
        self.link_crash = 'https://blaze.com/pt/games/crash'
        self.chorme_options = Options()
        self.chorme_options.add_argument("--no-sandbox") # linux only
        self.chorme_options.add_argument("--headless")
        self.d = webdriver.Chrome(LOCATION_CHROME_DRIVER_LINUX, options=self.chorme_options) 

    def append_list_as_row(self,file_name, list_of_elem):
        # Open file in append mode
        with open(file_name, 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow(list_of_elem)

    def colhe_dados(self):
        driver = self.d
        driver.get(self.link_crash)
        sleep(4)
        div_data = driver.find_element_by_class_name('entries')
        data = driver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[3]/div[2]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div[1]/span[1]').text
        print(data)
        while True:
            # for x in div_data:
            #     x.find_element_by_xpath('.//div[@class="title"]/a')
            try:
                data_new = driver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[3]/div[2]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div[1]/span[1]').text
            except NoSuchElementException as exc:
                print(exc)
                driver.get(self.link_crash)
                sleep(4)
                continue
            if data != data_new:
                print(data_new)
                row = [data_new, datetime.now()]
                self.append_list_as_row('data.csv', row)
                data = data_new
            sleep(3)
                
        

if __name__ == '__main__':
     blazer = Blazer()
     blazer.colhe_dados()