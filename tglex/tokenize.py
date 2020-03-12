"""Tokenize telegram messages."""

from typing import List

from tglex import message
from tglex import token


def tokenize(msg: message.Message) -> List[token.Token]:
    """Tokenize message."""
    return [token.Token(text=x) for x in msg.text.split()]
