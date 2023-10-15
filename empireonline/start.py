""" https://www.udemy.com/course/100-days-of-code/ """
import bs4
from collections import namedtuple
import html
import requests

Movie = namedtuple('Movie', 'title rank')

def get_data(content):
    soup = bs4.BeautifulSoup(content, 'html.parser')
    movie_list = []
    for item in soup.find_all(name='h3', class_='listicleItem_listicle-item__title__hW_Kn'):
        item = item.getText().split(')')
        rank = int(item[0])
        title = html.unescape(item[1].strip())
        movie_list.append(Movie(title, rank))
    return sorted(movie_list, key=lambda movie: movie.rank)

def main():
    """ main function """
    url = 'https://www.empireonline.com/movies/features/best-movies-2/'
    content = requests.get(url).text
    movie_list = get_data(content)
    with open('movies.txt', 'w', encoding='utf8') as txtfile:
        txtfile.writelines([f'{movie.rank}) {movie.title}\n' for movie in movie_list])


if __name__ == "__main__":
    import os
    import sys
    os.system('cls')
    print('-----------------------------------------------------------')
    main()
    sys.exit()
