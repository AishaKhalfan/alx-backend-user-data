#!/usr/bin/env python3
"""
Main file
"""
import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.FIELDS = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Formats a log message in a human-readable format.

        Arguments:
            record: a log record object

        Returns:
            a formatted string
        """
        logging.basicConfig(format=self.FORMAT)
        return(filter_datum(self.FIELDS, self.REDACTION,
                            super().format(record), self.SEPARATOR))


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Returns the log message obfuscated.
    Args:
        fields: a list of strings representing all fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        message: a string representing the log line
        separator: a string representing by which character is separating
    """

    for i in fields:
        message = re.sub(i + "=.*?" + separator, i + "=" + redaction
                         + separator, message)
    return message
