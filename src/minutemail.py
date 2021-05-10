import requests
from endpoints import NEW_EMAIL, MESSAGE_AFTER


class Mail(object):
    def __init__(self):
        self.session = requests.session()
        self.message_count = 0
        self.mail = self.session.get(NEW_EMAIL).json()['address']

    def get_mail(self):
        return self.mail

    def get_message(self):
        res = self.session.get(MESSAGE_AFTER+str(self.message_count)).json()
        if len(res) !=0:
            print(res, len(res), "adsf")

    def __str__(self):
        return self.mail


if __name__ == "__main__":
    mail = Mail()
    print(mail.get_mail())
    while True:
        mail.get_message()
