import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
        message: str, separator: str):
    """ returns the log message obfuscated:"""
    for i in fields:
        message = re.sub(i + "=.*?" + separator, i + "=" + redaction
                         + separator, message)
    return message

fields = ["password", "date_of_birth"]
messages = ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;", "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))
