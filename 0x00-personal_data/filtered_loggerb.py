#!/usr/bin/env python3
""" 0. Regex-ing module. """
from typing import List
import logging
import re


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Constructor of class RedactingFormatter. """
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
    # for i in fields:
    #     message = re.sub(i + "=.*?" + separator, i + "=" + redaction
    #                      + separator, message)
    # return(message)
    for f in fields:
        message = re.sub(f'{f}=.*?{separator}',
                         f'{f}={redaction}{separator}', message)
    return message


def get_logger() -> logging.Logger:
    """takes no arguments and returns a logging.Logger object."""
    logging.getLogger(name="user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    formatter = RedactingFormatter(PII_FIELDS)

    # Create a stream handler
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger
