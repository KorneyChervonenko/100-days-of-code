""" Send Email (smtplib) from https://www.udemy.com/course/100-days-of-code/ """
import smtplib
from email.header import Header
from email.mime.text import MIMEText


def main():
    """ main function """

    sender_email = 'example@gmail.com' # sender email
    sender_email_password = 'password' # пароль приложения
    recipient_email = 'example@yahoo.com'

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_email_password)
        subject = 'Hello, World!'
        # text = 'The quick brown fox jumps over the lazy dog'
        text = 'Съешь ещё этих мягких французских булок, да выпей же чаю'

        mime = MIMEText(text, 'plain', 'utf-8')
        mime['Subject'] = Header(subject, 'utf-8')

        # server.sendmail(sender_email, recipient_email, f'Subject:{subject}\n{text}')
        server.sendmail(sender_email, recipient_email, mime.as_string())


if __name__ == "__main__":
    import os
    import sys
    os.system('cls')
    print('-----------------------------------------------------------')
    main()

    sys.exit()
