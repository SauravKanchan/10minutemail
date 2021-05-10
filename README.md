# 10MinuteMail
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/python-10minutemail)
![APM](https://img.shields.io/apm/l/vim-mode)

Python wrapper for [10minutemail](https://10minutemail.com/)

### Installation

```
pip install python-10minutemail
```

### Usage

```python
from minutemail import Mail
import time

# Create a new 10 minute mail
mail = Mail()
print(mail)

# Keep on checking for a new mail/message
while True:
    if mail.new_message():  # Check for new mail
        print(mail.fetch_message())  # Fetch all the messages
    time.sleep(2)
```

### Sample message list

```json
[
  {
    "read": false,
    "expanded": false,
    "forwarded": false,
    "repliedTo": false,
    "sentDate": "2021-05-10T07:32:41.000+0000",
    "sentDateFormatted": "May 10, 2021, 7:32:41 AM",
    "sender": "sauravnk30@gmail.com",
    "from": "[Ljavax.mail.internet.InternetAddress;@37e8c463",
    "subject": "Test message",
    "bodyPlainText": "Test description\r\n",
    "bodyHtmlContent": "<div dir=\"ltr\">Test description</div>\r\n",
    "bodyPreview": "Test description\r\n",
    "id": "2118940165622869807"
  }, 
  ...
]
```

> Warning: If you use this tool/API 