""" get trivia quiz data https://www.udemy.com/course/100-days-of-code/ """
from collections import namedtuple

# from pprint import pprint
import requests

Question = namedtuple('Question', 'category, correct_answer, difficulty, incorrect_answers, question, type')

def get_quiz_data(link: str) -> dict:
    """ get quiz data """
    response = requests.get(url=link)
    response.raise_for_status()
    data = response.json()
    if data.get('response_code') != 0:
        print('fail')
        return None
    return [Question(**question) for question in data.get('results')]

def main():
    """ main function """
    # get_quiz_data()
    questions = get_quiz_data('https://opentdb.com/api.php?amount=3')
    for question in questions:
        print('-------------------')
        print(question, sep='\n')
        print('-------------------')


if __name__ == "__main__":
    import os
    import sys
    os.system('cls')
    print('-----------------------------------------------------------')
    main()

    sys.exit()
