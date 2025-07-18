from dotenv import load_dotenv
import os
from requests import post, get
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

load_dotenv()

news_id = os.getenv("NEWS_ID")

def get_article_news():
    url = f"https://newsapi.org/v2/top-headlines?sources=cnn&apiKey={news_id}"
    result = get(url)
    json_result = json.loads(result.content)
    return json_result

def get_content_news():
    print("Content:")

    for idx, articls in enumerate(article['articles']):
        print(f"{idx + 1}. {article['articles'][idx]['description']}")

def get_url():
    links = []
    for idx, urs in enumerate(article['articles']):
         links.append(article['articles'][idx]['url'])

    return links


article = get_article_news()
url = get_url()

def get_html():
    with urlopen(url[0]) as responce:
        content = responce.read()

    soup = bs(content, 'html.parser')
    article_body = soup.find(class_='article__content')
    text = [p.find(string=True) for p in soup.find_all('p')]

    par = []
    for p in text:
        par.append(p.get_text(strip=True))

    p = filter(None, par)
    data = []

    for x in p:
        data.append(x)

    return data

article_text = get_html()

def convert_json():
    data = []
    i = 0
    for par in article_text:
        key = f"{i + 1}"
        data.append({f"{key}" : f"{par}"})
        i += 1

    return data

convert = convert_json()

data = {
        "text" : convert
    }

# def full_creation():
#     for i in range(len(url)):
#

def create_json():
        json_filename = "Artircles.json"
        json_path = f"/home/kayaki/web/wiki/src/json/{json_filename}"

        with open(json_path, "w") as json_file:
            json.dump(data, json_file, indent=4)

        print(f"File written to: {json_path}")

def main():
    full_creation()



if __name__ == "__main__":
    main()
