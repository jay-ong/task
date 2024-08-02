import requests
from bs4 import BeautifulSoup
from scraper.models import Movie


def scrape_movie():
    gogoflix = scrape_gogoflix()
    fmoviesz = scrape_fmoviesz()

    movies = gogoflix + fmoviesz

    return movies

def scrape_gogoflix():
    url = "https://gogoflix.pro/"
    endpoint = url.rsplit("/", 1)[0]
    response = requests.get(url)
    scraped_data = {
        'endpoint': url,
        'task_name': 'search_web_page',
        'errors': []
    }
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        scraped_data['success'] = True
        scraped_data['status'] = 'success'
        movie_items = []
        for item in soup.select('.cat-item'):
            title = item.select_one('.title').get_text()
            link_title = item.select_one('.link-title').get('href')
            poster = item.select_one('.poster').find("img").get('src')
            text_tags = item.select_one('.text').find_all("span")

            tags =  [i.get_text().split(',') for i in text_tags]
            tags = [i for sublist in tags for i in sublist]
            movie_items.append({
                'title': title,
                'link_title': f'{endpoint}{link_title}',
                'poster': f'{endpoint}{poster}',
                'tags': tags
            })
        
        scraped_data['result'] =  {
            'total_items': len(movie_items),
            'items': movie_items
        }
        Movie.objects.create(**scraped_data)

        return movie_items
    else:
        scraped_data['success'] = False
        scraped_data['status'] = 'failed'
        scraped_data['result'] = {}
        scraped_data['errors'] = ['failed']
        return []
    
def scrape_fmoviesz():
    url = "https://fmoviesz.bz/"
    response = requests.get(url)
    scraped_data = {
        'endpoint': url,
        'task_name': 'search_web_page',
        'errors': []
    }
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        scraped_data['success'] = True
        scraped_data['status'] = 'success'
        movie_items = []
        for item in soup.select('.movies'):
            title = item.select_one('.Title').get_text()
            link_title = item.select_one('.TPost').find("a").get('href')
            poster = item.select_one('.Image').find("img").get('src')
            tags = [i.get_text() for i in item.select_one('.Genre').find_all('a')]

            movie_items.append({
                'title': title,
                'link_title': link_title,
                'poster': poster,
                'tags': tags
            })
        
        scraped_data['result'] =  {
            'total_items': len(movie_items),
            'items': movie_items
        }
        Movie.objects.create(**scraped_data)

        return movie_items
    else:
        scraped_data['success'] = False
        scraped_data['status'] = 'failed'
        scraped_data['result'] = {}
        scraped_data['errors'] = ['failed']
        return []