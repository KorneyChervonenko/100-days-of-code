""" https://www.udemy.com/course/100-days-of-code/  and  
https://blog.codinghorror.com/password-rules-are-bullshit/ """
import string
import random
import itertools
import collections
# import pandas as pd

password_base_files = ['10-million-password-list-top-100000.txt',
                        'ncsc.gov.uk_static-assets_documents_PwnedPasswordsTop100k.txt',
                        '10-million-password-list-top-1000000.txt']
char_sets = (string.digits, string.ascii_letters, string.punctuation)
char_source = ''.join(char_sets)

def generate_password(length: int = 8, chararacters: str = char_source):
    """ generate new password """
    # char_source = string.digits + string.ascii_letters + string.punctuation
    # char_source = ''.join(char_sets)
    while True:
        password = ''
        while len(password) < length:
            password += random.choice(chararacters)
            if len(password) > 2:
                last3chars = password[-3:]
                # must not include aaa, 111 or abc, 123
                # if len(set(last3chars)) == 1 or last3chars in char_source:
                if include_more_than_2_identical_chars(password) or last3chars in chararacters:
                    password = password[:-1]
        if is_correct(password):
            return password

def is_commonly_used(password: str) -> bool:
    """ check if password in list of most commonly used """
    for file in password_base_files:
        with open(file, 'r', encoding='utf-8') as data:
            for line in data:
                if password == line.strip():
                    return True
    return False

def get_new_password(length: int = 8) -> str:
    """ generate new password and check if it is not commonly used """
    while True:
        password = generate_password(length)
        if is_correct(password):
            return password

def test_is_commonly_used():
    """ test """
    passwords = {'michael', 'football', 'iloveyou', 'letmein', 'Pf?G*a4H,=&E.HO]t(e0',
                 'aFAx5m9RS3kz!r)LA]s', 'Tr0ub4dor&3', '123123123', 'q1w2e3r4',
                 'оченьсложныйпароль', 'newpassword', 'abcabcabcabc', 'opqrst', '999999999999999',}
    for password in passwords:
        print(password,['is not', 'is', ][is_commonly_used(password)], 'commonly used')

def include_char_from_charset(password: str, charset) -> bool:
    """ check if there is at least one character from charset is in the password """
    return bool(set(password).intersection(charset))

def include_2chars_from_different_charset(password: str, char_sets: tuple) -> bool:
    """ check if there are at least two chars from different charsets are in the password """
    for charset1, charset2 in itertools.combinations(char_sets, 2):
        if include_char_from_charset(password, charset1) and include_char_from_charset(password, charset2):
            return True
    return False

def include_more_than_2_identical_chars(password: str) -> bool:
    """ check if there are more than 2 identical chars are in the password """
    if len(password) > 2:
        char, count = collections.Counter(password).most_common(1)[0]
        # print(char, count)
        return count > 2
    return False

def include_more_than_2_consecutive_chars(password: str, chararacters: str = char_source) -> bool:
    """ check if there are more than 2 consecutive chars are in the password """
    if len(password) > 2:
        for i, ch in enumerate(password[1:-1], 1):
            triplet = password[i-1] + ch + password[i+1]
            if triplet in chararacters:
                # print(triplet)
                return True
    return False

def is_correct(password: str) -> bool:
    """ check if password fits the rules """
    return all((include_2chars_from_different_charset(password, char_sets),
                not is_commonly_used(password),
                7 < len(password) < 33,
                not include_more_than_2_identical_chars(password),
                not include_more_than_2_consecutive_chars(password),
                ))

def test():
    """ test """
    assert include_char_from_charset('abc^^^123', string.ascii_letters) is True
    assert include_char_from_charset('abc^^^123', string.digits) is True
    assert include_char_from_charset('abc^^^123', string.punctuation) is True
    assert include_char_from_charset("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""", string.punctuation) is True

    assert include_char_from_charset('^^^123', string.ascii_letters) is False
    assert include_char_from_charset('abc^^^', string.digits) is False
    assert include_char_from_charset('abc123', string.punctuation) is False

    assert include_2chars_from_different_charset('123###', char_sets) is True
    assert include_2chars_from_different_charset('123abc', char_sets) is True
    assert include_2chars_from_different_charset('^^^abc', char_sets) is True
    assert include_2chars_from_different_charset('123^^^abc', char_sets) is True

    assert include_2chars_from_different_charset('abc', char_sets) is False
    assert include_2chars_from_different_charset('123123123', char_sets) is False
    assert include_2chars_from_different_charset("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""", char_sets) is False

    assert include_more_than_2_identical_chars('abcaa') is True
    assert include_more_than_2_identical_chars('ab111caa') is True
    assert include_more_than_2_identical_chars('#ab#ca#') is True
    assert include_more_than_2_identical_chars('abca') is False
    assert include_more_than_2_identical_chars('1abca1') is False
    assert include_more_than_2_identical_chars("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""") is False

    assert include_more_than_2_consecutive_chars('qwertabcasdf123') is True
    assert include_more_than_2_consecutive_chars("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""") is True
    assert include_more_than_2_consecutive_chars('###############') is False
    assert include_more_than_2_consecutive_chars('321cba') is False
    
    assert is_correct('b1#a^2cc3') is True

    print('All tests were performed')


def main():
    """ main function """
    new_password = get_new_password(15)
    print(f'password: {new_password}, length: {len(new_password)}')



if __name__ == "__main__":
    import sys
    import os
    os.system('cls')
    print('-----------------------------------------------------------')
    # main()
    test()

    sys.exit()
