import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '..', 'aggrenews_project', '.env'))

class Kompas:
    def __init__(self):
        self.name = "Kompas"
        self.media_name = []
        self.title = []
        self.link = []
        self.date= []
        self.bodytext = []
        self.imgSrc = []

    def scrape_search(self, search):
        Google_Developer_Key = os.getenv('GOOGLE_DEV_KEY')
        Kompas_cx = '018212539862037696382:-xa61bkyvao'        
        response = requests.get("https://www.googleapis.com/customsearch/v1?key=" + Google_Developer_Key + "&cx=" + Kompas_cx + "&q=" + search + "&sort=date") 
        response.raise_for_status()        
        articles = response.json()['items']
        

        for article in articles:                        
            self.media_name.append(self.name)
            newLink = ''
            self.title.append(article['title'])
            if ("url=" in article['link']):
                newLink = article['link'].split('url=')[1]     
            else:
                newLink = article['link']                
            self.link.append(newLink)
            self.imgSrc.append(article['pagemap']['cse_thumbnail'][0]['src'])
            result = self.scrape_article(newLink)
            self.bodytext.append(result['bodyText'])
            self.date.append(result['date'])
            
    def scrape_article(self, link):
            
        body = ""
        date = ""
        
        response = requests.get(link)
        soup = BeautifulSoup(response.content, 'html5lib')
        
        if (soup.find('div', class_='read__content')):
            paras = soup.find('div', class_='read__content').find_all('p')
            for para in paras:            
                body = body + " " + para.get_text()

        dateElement = soup.find('div', class_='read__time')
        if dateElement:
            date = dateElement.get_text()
            #Kompas.com - 08/05/2021, 12:59 WIB
            date = date.split(' - ')[1]
            date = date.split(',')[0]
            day,month,year = date.split('/')            
            date = year + '-' + month + '-' + day

        return {"bodyText": body, 'date': date} 

    def get_variables(self):
        return {
            'name': self.media_name,
            'title': self.title,
            'link': self.link,
            'date': self.date,
            'body': self.bodytext,
            'imgSrc': self.imgSrc
        }
