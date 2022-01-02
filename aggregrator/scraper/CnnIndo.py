import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os


class CnnIndo:
    def __init__(self):
        self.name = "CNN Indonesia"
        self.media_name = []
        self.title = []
        self.link = []
        self.date= []
        self.bodytext = []
        self.imgSrc = []

    def scrape_search(self, search):
        print(os.getcwd())                
        chromedriver_path = os.getcwd() + '/aggregrator/scraper/chromedriver'
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        driver = webdriver.Chrome(executable_path=chromedriver_path,
                                    chrome_options=chrome_options)        
        driver.get('https://www.cnnindonesia.com/search/?query=' + search)
        articles = driver.find_elements(By.CSS_SELECTOR, "article:not([class])")

        for article in articles: 
            self.media_name.append(self.name)                       
            self.title.append(article.find_element(By.CSS_SELECTOR, '.title').get_attribute('innerText')         )
            self.imgSrc.append(article.find_element(By.CSS_SELECTOR, 'img').get_attribute('src'))
            linkNew = article.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
            self.link.append(article.find_element(By.CSS_SELECTOR, 'a').get_attribute('href'))
            result = self.scrape_article(linkNew)
            self.bodytext.append(result["bodyText"])
            self.date.append(result['date'])            
        
        driver.quit()

    def scrape_article(self, link):
        print(link)
        date = ""
        body = ""

        response = requests.get(link)
        soup = BeautifulSoup(response.content, 'html5lib')

        if soup.find('div', id='detikdetailtext'):
            paras = soup.find('div', id='detikdetailtext').find_all('p')                
            for para in paras:
                body = body + " " + para.get_text()

        dateElement = soup.find('div', class_='content_detail').find('div', class_='date')
        if dateElement:            
            date = dateElement.get_text()                        
            if (date.find('CNN Indonesia') == -1):
                # Senin, 27 Dec 2021 20:01 WIB
                day,month,year,*time = date.split(', ')[1].split(' ')
                date = year + self.change_month(month) + day  
            else:
                date = ''    

        return {"bodyText": body, 'date': date} 

    def change_month(self, month):
        if (month == "Jan"):
            month = "-01-"
    
        elif (month == "Feb"):
            month = "-02-"
    
        elif (month == "Mar"):
            month = "-03-" 
    
        elif (month == "Apr"):
            month = "-04-"
    
        elif (month == "Mei" or month == "May"):
            month = "-05-"
    
        elif (month == "Jun"):
            month = "-06-"
    
        elif (month == "Jul"):
            month = "-07-"
    
        elif (month == "Agu" or month == "Aug"):
            month = "-08-"
    
        elif (month == "Sep"):
            month = "-09-"
    
        elif (month == "Okt" or month == "Oct"):
            month = "-10-"
    
        elif (month == "Nov"):
            month = "-11-"
    
        elif (month == "Dec"):
            month = "-12-"
    
        else:
            month = month
    
        return month
    
    def get_variables(self):
        return {
            'name': self.media_name,
            'title': self.title,
            'link': self.link,
            'date': self.date,
            'body': self.bodytext,
            'imgSrc': self.imgSrc
        }