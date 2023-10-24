
import requests

def get_news(country, api_key='bd360e94249945b69f6a1e22c16a50cb'):
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"TITLE\n', {article['title']}, '\nDESCRIPTION\n', {article['description']}")
    return results


print(get_news(country='us'))
