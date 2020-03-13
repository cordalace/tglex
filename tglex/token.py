"""Token entities."""

import dataclasses
from typing import Optional


@dataclasses.dataclass(frozen=True)
class Token:
    """Token."""

    text: str


@dataclasses.dataclass(frozen=True)
class CommaToken(Token):
    """Comma token."""


@dataclasses.dataclass(frozen=True)
class QuestionToken(Token):
    """Question token."""


@dataclasses.dataclass(frozen=True)
class DotToken(Token):
    """Dot (sentence end) token."""


@dataclasses.dataclass(frozen=True)
class MentionToken(Token):
    """Telegram user mention token."""

    user_id: Optional[int]
    username: Optional[str]


@dataclasses.dataclass(frozen=True)
class HashtagToken(Token):
    """Hashtag token."""


@dataclasses.dataclass(frozen=True)
class CashtagToken(Token):
    """Cashtag token."""


@dataclasses.dataclass(frozen=True)
class BotCommandToken(Token):
    """Bot command token."""


@dataclasses.dataclass(frozen=True)
class URLToken(Token):
    """URL token."""


@dataclasses.dataclass(frozen=True)
class EmailToken(Token):
    """Email token."""
