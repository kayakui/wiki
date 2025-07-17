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
    with urlopen(url[4]) as responce:
        content = responce.read()

    soup = bs(content, 'html.parser')
    article_body = soup.find(class_='article__content')
    # text = [p.find(string=True) for p in soup.find_all('p')]

    par = []
    data = []

    for i in article_body:
        par.append(article_body.get_text(strip=True))
        # data.append(par)
        # print(par)


    return article_body


# def format_html():
#     if
# def get_html():
#     with urlopen(url[3]) as responce:
#         content = responce.read()
#
#     soup = bs(content, 'html.parser')
#     article_body = soup.find_all(class_='article')
#     if article_body:
#         text = [p.find(string=True, recursive=False) for p in soup.find_all('p')]
#     par = []
#
#     for i, para in enumerate(text):
#         par.append(f"{para}")
#
#     # print(par)
#     return par
#
article_text = get_html()
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

# def full_creation():
#     num = 0
#     for i in range(len(url)):
#         try:
#             with urlopen(url[num]) as responce:
#                 content = responce.read()
#
#             soup = bs(content, 'html.parser')
#             article_body = soup.find_all(class_='article-body__content')
#             text = [p.find(string=True, recursive=False) for p in soup.find_all('p')]
#             par = []
#
#             for i, para in enumerate(text):
#                 par.append(f"{para}")
#
#             json_conv = []
#             for i, text in enumerate(par):
#                 key = f"p{i+1}"
#                 json_conv.append({key: text})
#
#             data = {}
#             for i, text in enumerate(json_conv):
#                 data.update({
#                         f"text{count + 1}" : f"{json_conv[count]}"
#                         })
#
#                 num += 1
#


        # except Exception:
        #     num += 1
        #     # print(f"{num}DUMASS")
        #     pass
        #
        # return json_conv

# data = full_creation()
#
# def create_json():
#         json_filename = f"Artircle3.json"
#         json_path = f"/home/kayaki/web/wiki/src/json/{json_filename}"
#
#         with open(json_path, "w") as json_file:
#             json.dump(data, json_file, indent=4)
#
#         print(f"File written to: {json_path}")


def main():
    # full_creation()
    # create_json()
    print(article_text)



if __name__ == "__main__":
    main()
