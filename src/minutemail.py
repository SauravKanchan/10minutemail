import requests
from endpoints import NEW_EMAIL, MESSAGE_AFTER, MESSAGE_COUNT
from fake_useragent import UserAgent

class Mail(object):
    """
    Python wrapper for 10minutemail.com
    """

    def __init__(self):
        self.session = requests.session()
        self.session.headers = {'user-agent': UserAgent().random}
        self.message_count = 0
        self.messages = []
        self.mail = self.session.get(NEW_EMAIL).json()['address']

    def get_mail(self):
        """
        :return: Mail of the current instance
        """
        return self.mail

    def get_message(self):
        """
        :return: list of messages stored in this instance
        """
        return self.messages

    def fetch_message(self):
        """
        Fetches for new messages which are not present in the instance
        :return: List of messages stored in the instance
        """
        res = self.session.get(MESSAGE_AFTER + str(self.message_count)).json()
        self.message_count += len(res)
        self.messages += res
        return self.messages

    def new_message(self):
        """
        Check whether there are new messages or not
        :return: bool
        """
        return self.session.get(MESSAGE_COUNT).json()['messageCount'] != self.message_count

    def __str__(self):
        return self.mail


if __name__ == "__main__":
    import time
    mail = Mail()
    print(mail.get_mail())
    while True:
        time.sleep(2)
