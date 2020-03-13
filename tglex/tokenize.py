"""Tokenize telegram messages."""

from typing import Generator, Optional, Tuple

from tglex import message
from tglex import token


def split_entity_parts(
        msg: message.Message,
) -> Generator[Tuple[str, Optional[message.MessageEntity]], None, None]:
    """Split message into parts according to entities."""
    offset_shift = 0
    text = msg.text
    for i, entity in enumerate(sorted(msg.entities, key=lambda e: e.offset)):
        start = entity.offset + offset_shift
        end = start + entity.length
        entity_text = text[start:end]

        before, after = text[:start], text[end:]
        text = after
        offset_shift -= entity.offset + entity.length

        if before:
            yield before, None
        yield entity_text, entity
        if len(msg.entities) == i + 1 and after:  # last entity
            yield after, None

    if not msg.entities:
        yield msg.text, None


def tokenize(msg: message.Message) -> Generator[token.Token, None, None]:
    """Tokenize message."""
    for part_text, entity in split_entity_parts(msg):
        if entity is None:
            yield from (token.Token(text=x) for x in part_text.split())
        elif entity.type == message.MessageEntityType.MENTION:
            yield token.MentionToken(
                text=part_text,
                username=part_text,
                user_id=None,
            )
        elif entity.type == message.MessageEntityType.HASHTAG:
            yield token.HashtagToken(text=part_text)
        elif entity.type == message.MessageEntityType.CASHTAG:
            yield token.CashtagToken(text=part_text)
        elif entity.type == message.MessageEntityType.BOT_COMMAND:
            yield token.BotCommandToken(text=part_text)
        elif entity.type == message.MessageEntityType.URL:
            yield token.URLToken(text=part_text)
        elif entity.type == message.MessageEntityType.EMAIL:
            yield token.EmailToken(text=part_text)
