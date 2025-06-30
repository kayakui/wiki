from dotenv import load_dotenv
import os
from requests import post, get
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

load_dotenv()

news_id = os.getenv("NEWS_ID")
york_id = os.getenv("NEWYORK_ID")

def get_most_shared_fb_york():
    url = f"https://api.nytimes.com/svc/mostpopular/v2/shared/1/facebook.json?api-key={york_id}"
    result = get(url)
    json_result = json.loads(result.content)
    return json_result

def sort_titles_york():
    print("Titles:")

    for idx, title in enumerate(shared['results']):
        print(f"{idx + 1}. {shared['results'][idx]['title']}")

def get_abstracts_york():
    print("Descriptions:")

    for idx, abstracts in enumerate(shared['results']):
        print(f"{idx + 1}. {shared['results'][idx]['abstract']}")

def get_article_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_id}"
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

shared = get_most_shared_fb_york()
article = get_article_news()
url = get_url()

# num = 6
#
# def get_html():
#     with urlopen(url[num]) as responce:
#         content = responce.read()
#
#     soup = bs(content, 'html.parser')
#     article_body = soup.find_all(class_='article-body__content')
#     text = [p.find(string=True, recursive=False) for p in soup.find_all('p')]
#     par = []
#
#     for i, para in enumerate(text):
#         par.append(f"{para}")
#
#     # print(par)
#     return par
#
# article_text = get_html()
#
# def convert_json():
#     data = []
#     for i, text in enumerate(article_text):
#         key = f"p{i+1}"
#         data.append({key : text})
#
#     return data
#
# convert = convert_json()
#
# data = {
#         "text1" : convert
#     }
#
#
# def create_json():
#     json_filename = "test.json"
#     json_path = f"/home/kayaki/web/Wiki/src/json/{json_filename}"
#
#     with open(json_path, "w") as json_file:
#         json.dump(data, json_file, indent=4)
#
#     print(f"File written to: {json_path}")

def full_creation():
    num = 0
    ar_num = 1
    for i in range(len(url)):
        try:
            with urlopen(url[num]) as responce:
                content = responce.read()

            soup = bs(content, 'html.parser')
            article_body = soup.find_all(class_='article-body__content')
            text = [p.find(string=True, recursive=False) for p in soup.find_all('p')]
            par = []

            for i, para in enumerate(text):
                par.append(f"{para}")

            convert = []
            for i, text in enumerate(par):
                key = f"p{i+1}"
                convert.append({key : text})

            data = {
                "text" : convert
            }

            json_filename = f"Artircle{ar_num}.json"
            json_path = f"/home/kayaki/web/Wiki/src/json/{json_filename}"

            with open(json_path, "w") as json_file:
                json.dump(data, json_file, indent=4)

            print(f"File written to: {json_path}")
            num += 1
            ar_num += 1

        except Exception:
            num += 1
            ar_num += 1
            pass


def main():
    # full_creation()



if __name__ == "__main__":
    main()
