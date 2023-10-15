""" https://www.udemy.com/course/100-days-of-code/ """
from collections import namedtuple

import bs4
import requests

Article = namedtuple('Article', 'id rank score title link')

def get_highest_scored_article(content):
    soup = bs4.BeautifulSoup(content, 'html.parser')
    articles = []
    for tr_tag in soup.select(selector='tr .athing'):

        id = tr_tag.get('id')

        rank_tag = tr_tag.find(name='span',  class_='rank')
        rank = int(rank_tag.getText().strip('.'))

        title_tag = tr_tag.find(name='span',  class_='titleline').find(name='a')
        if title_tag:
            url = title_tag.get('href')
            title = title_tag.getText()
        else:
            url, title = None, None

        score_tag = soup.find(id='score_'+id)
        if score_tag:
            score = int(score_tag.getText().strip(' points'))
        else:
            score = 0

        article = Article(id, rank, score, title, url)
        articles.append(article)
    return max(articles, key=lambda article: article.score) 



def main():
    """ main function """
    url = 'https://news.ycombinator.com/news'
    content = requests.get(url).text
    highest_scored_article = get_highest_scored_article(content)
    print(highest_scored_article)

if __name__ == "__main__":
    import os
    import sys
    os.system('cls')
    print('-----------------------------------------------------------')
    main()
    sys.exit()
