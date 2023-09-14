""" Birthday wisher from https://www.udemy.com/course/100-days-of-code/ """
import datetime as dt
import os
import random
import smtplib
from email.header import Header
from email.mime.text import MIMEText

import pandas as pd


def get_letter_templates():
    """ scan letter_templates folder for files and return list of them """
    package_dir = os.path.dirname(os.path.abspath(__file__))
    template_directory_path = os.path.join(package_dir, 'letter_templates')
    file_list = []
    for file_name in os.listdir(template_directory_path):
        full_file_name = os.path.join(template_directory_path, file_name)
        if os.path.isfile(full_file_name):
            file_list.append(full_file_name)
    return file_list

def get_data_from_file(filename: str='birthdays.csv') -> dict:
    """ load data from file """
    try:
        csv_df = pd.read_csv(filename)
        for person in csv_df.itertuples():
            yield person
    except:
        print('something went wrong')
        return None

def construct_letter(person, template):
    """ construct letter to person from template """
    with open(template, 'r', encoding='utf-8') as template_file:
        first_line = template_file.readline()
        template_lines = template_file.readlines()
    personalized_first_line = first_line.replace('[NAME]', person.name)
    return personalized_first_line + ''.join(template_lines)

def send_letter(person, letter):
    """ send letter to person """
    sender_email = 'my_email@gmail.com' # sender email
    sender_email_password = 'google password' # пароль приложения
    recipient_email = person.email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_email_password)
        subject = f'Letter of congratulations to {person.name}'
        mime = MIMEText(letter, 'plain', 'utf-8')
        mime['Subject'] = Header(subject, 'utf-8')
        server.sendmail(sender_email, recipient_email, mime.as_string())    

def main():
    """ main function """

    today = dt.datetime.now()
    for person in get_data_from_file():
        if (today.month, today.day) == (person.month, person.day):
            file_list = get_letter_templates()
            template = random.choice(file_list)
            letter_to_person = construct_letter(person, template)
            send_letter(person, letter_to_person)


if __name__ == "__main__":
    import os
    import sys
    os.system('cls')
    print('-----------------------------------------------------------')
    main()
    sys.exit()

