import requests
from endpoints import NEW_EMAIL, MESSAGE_AFTER, MESSAGE_COUNT


class Mail(object):
    def __init__(self):
        self.session = requests.session()
        self.message_count = 0
        self.messages = []
        self.mail = self.session.get(NEW_EMAIL).json()['address']

    def get_mail(self):
        return self.mail

    def get_message(self):
        return self.messages

    def fetch_message(self):
        res = self.session.get(MESSAGE_AFTER + str(self.message_count)).json()
        self.message_count += len(res)
        self.messages += res
        return self.messages

    def new_message(self):
        return self.session.get(MESSAGE_COUNT).json()['messageCount'] != self.message_count

    def __str__(self):
        return self.mail


if __name__ == "__main__":
    import time
    mail = Mail()
    print(mail.get_mail())
    while True:
        time.sleep(2)
