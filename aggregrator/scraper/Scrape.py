from .Detik import Detik
from .Kompas import Kompas
from .CnnIndo import CnnIndo

class Scrape: 
    @staticmethod
    def scrape(search_word):

        newDetik = Detik()
        newDetik.scrape_search(search_word)

        newKompas = Kompas()
        newKompas.scrape_search(search_word)

        newCnnIndo = CnnIndo()
        newCnnIndo.scrape_search(search_word)

        dict_news = {
            'Detik': newDetik.get_variables(),
            'Kompas': newKompas.get_variables(),
            'CnnIndo': newCnnIndo.get_variables()
        }

        return dict_news
