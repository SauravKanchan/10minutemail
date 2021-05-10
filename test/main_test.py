from minutemail import Mail
import re

mail = Mail()


def test_new_mail():
    regex = r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,7}$'
    assert (re.search(regex, mail.get_mail()) is not None)


def test_new_message():
    assert not mail.new_message()


def test_fetch_message():
    assert mail.fetch_message() == []
