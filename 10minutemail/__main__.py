import urllib.request, json
from endpoints import NEW_EMAIL


def fetch(url):
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers = {'User-Agent': user_agent, }
    request = urllib.request.Request(url, None, headers)
    response = urllib.request.urlopen(request)
    return json.loads(response.read().decode('utf-8'))


class Mail(object):
    def __init__(self):
        self.mail = fetch(NEW_EMAIL)['address']

    def get_mail(self):
        return self.mail

    def __str__(self):
        return self.mail


if __name__ == "__main__":
    mail = Mail()
    print(mail.get_mail())