"""Telegram message entity."""

import dataclasses
import datetime
import enum
from typing import List, Optional

# pylint: disable=invalid-name


class ChatType(enum.Enum):
    """Chat type."""

    PRIVATE = enum.auto()
    GROUP = enum.auto()
    SUPERGROUP = enum.auto()


@dataclasses.dataclass(frozen=True)
class User:
    """Telegram user or bot."""

    id: int
    is_bot: bool
    username: str


@dataclasses.dataclass(frozen=True)
class Chat:
    """Telegram chat."""

    id: int
    type: ChatType


class MessageEntityType(enum.Enum):
    """Message entity type."""

    MENTION = enum.auto()
    HASHTAG = enum.auto()
    CASHTAG = enum.auto()
    BOT_COMMAND = enum.auto()
    URL = enum.auto()
    EMAIL = enum.auto()
    PHONE_NUMBER = enum.auto()
    TEXT_MENTION = enum.auto()


@dataclasses.dataclass(frozen=True)
class MessageEntity:
    """Special entity in a text message."""

    type: MessageEntityType
    offset: int
    length: int
    user: Optional[User]


@dataclasses.dataclass(frozen=True)
class Message:
    """Telegram message."""

    message_id: int
    message_from: User
    chat: Chat
    date: datetime.datetime
    text: str
    entities: List[MessageEntity]
