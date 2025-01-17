import scrapy
from urllib.parse import urlencode
import requests

API_KEY = '14a3b8f9-1492-4df4-beb7-c60a6f85a0c8'


class FilmaffinitySpiderSpider(scrapy.Spider):
    # Realiza una solicitud inicial usando la API de scrapeops para obtener el contenido de la página con proxy
    response = requests.get(
        url='https://proxy.scrapeops.io/v1/',
        params={
            'api_key': API_KEY,
            'url': 'https://m.filmaffinity.com/es/ranking.php?rn=ranking_fa_movies', 
        },
    )
    
    name = "filmaffinity-spider"
    allowed_domains = ["m.filmaffinity.com"]
    start_urls = ["https://m.filmaffinity.com/es/ranking.php?rn=ranking_fa_movies"]

    # Método principal que procesa la respuesta de la página extraída de la página filmaffinity
    def parse(self, response):

        movies= response.css('li.list-group-item.grid-item')
        print(response.headers)
        
        print("Longitud lista: ", len(movies))

        for movie in movies:
            print(movie.css('div.mc-title::text').get())
            title=movie.css('div.mc-title::text').get()
            ranking=movie.css('div.avgrat-box.in-block::text').get()
            actor=movie.css('li.mc-cast::text').get()
            directed=movie.css('li.mc-director::text').getall()[0]
            yield {
                'Title': title,
                'Ranking': ranking,
                'Actor': actor,
                'Directed': directed

            }