import requests

r = requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2023-10-01&to=2023-10-10&sortBy=popularity&language=en&apiKey=bd360e94249945b69f6a1e22c16a50cb')

# implement debugiing to udnertsand data structure
content = r.json()
# print(type(content))
# print(content['articles'])

articles = content['articles']

for article in articles:
    print('TITLE\n', article['title'], '\nDESCRIPTION\n', article['description'])

def get_news(topic, from_date, to_date, language='en', api_key='bd360e94249945b69f6a1e22c16a50cb'):
    url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}'
