"""Telegram message entity."""

import dataclasses
import datetime
import enum

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


@dataclasses.dataclass(frozen=True)
class Message:
    """Telegram message."""

    message_id: int
    message_from: User
    chat: Chat
    date: datetime.datetime
    text: str
