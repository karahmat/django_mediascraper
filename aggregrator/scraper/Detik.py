import requests
from bs4 import BeautifulSoup

class Detik:
    def __init__(self):
        self.name = "Detik"
        self.media_name = []
        self.title = []
        self.link = []
        self.date= []
        self.bodytext = []
        self.imgSrc = []

    def scrape_search(self, search):
        response = requests.get("https://www.detik.com/search/searchnews?query=" + search + "&sortby=time&page=1")
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html5lib')
        articles = soup.find_all('article')
        for article in articles:
            self.media_name.append(self.name)
            self.title.append(article.h2.string)            
            self.link.append(article.a.get('href'))
            self.imgSrc.append(article.span.span.img.get('src'))            
            result = self.scrape_article(article.a.get('href'))
            self.bodytext.append(result["bodyText"])
            self.date.append(result['date'])

    def scrape_article(self, link):
        date = ""
        body = ""       

        response = requests.get(link)
        soup = BeautifulSoup(response.content, 'html5lib')

        if ("health.detik.com" in link or "travel.detik.com" in link):
            paras = soup.find('div', id='detikdetailtext').find_all('p')
            for para in paras:
                body = body + " " + para.get_text()

        elif ("inet.detik.com" in link):
            paras = soup.find('div', class_="itp_bodycontent detail__body-text").find_all('p')
            for para in paras:
                body = body + " " + para.get_text()

        else:
            if (soup.find('div', class_='detail__body-text itp_bodycontent')):
                paras = soup.find('div', class_='detail__body-text itp_bodycontent').find_all('p')  
                for para in paras:
                    body = body + " " + para.get_text()      

        dateElement = soup.find('div', class_='detail__date')
        if dateElement:
            date = dateElement.get_text()
            day,month,year,*time = date.split(', ')[1].split(' ')
            date = year + self.change_month(month) + day     

        else:
            if (soup.find('div', class_='date')):
                date = soup.find('div', class_='date').get_text()
                day,month,year,*time = date.split(', ')[1].split(' ')
                date = year + self.change_month(month) + day  
            else:
                date = soup.find('span', class_='date').get_text()
                day,month,year,*time = date.split(', ')[1].split(' ')
                date = year + self.change_month(month) + day  


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
    
        elif (month == "Mei"):
            month = "-05-"
    
        elif (month == "Jun"):
            month = "-06-"
    
        elif (month == "Jul"):
            month = "-07-"
    
        elif (month == "Agu" or month == "Aug"):
            month = "-08-"
    
        elif (month == "Sep"):
            month = "-09-"
    
        elif (month == "Okt"):
            month = "-10-"
    
        elif (month == "Nov"):
            month = "-11-"
    
        elif (month == "Des"):
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