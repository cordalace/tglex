import dataclasses
import datetime

import pytest

import tglex
from tglex.tokenize import tokenize_usual_text

BASE_MESSAGE = tglex.Message(
    message_id=42,
    message_from=tglex.User(
        id=43,
        is_bot=False,
        username='@user',
    ),
    chat=tglex.Chat(
        id=44,
        type=tglex.ChatType.GROUP,
    ),
    date=datetime.datetime.utcnow(),
    text='Test text here',
    entities=[],
)


def test_tokenize():
    msg = dataclasses.replace(BASE_MESSAGE, text='Hello world')
    assert list(tglex.tokenize(msg)) == [
        tglex.Token('Hello'),
        tglex.Token('world'),
    ]


@pytest.mark.parametrize('text,entity_type,expected_token', [
    ('word', None, tglex.Token('word')),
    (
        '@user',
        tglex.MessageEntityType.MENTION,
        tglex.MentionToken(text='@user', user_id=None, username='@user'),
    ),
    (
        '#пентон',
        tglex.MessageEntityType.HASHTAG,
        tglex.HashtagToken('#пентон'),
    ),
    (
        '$USD',
        tglex.MessageEntityType.CASHTAG,
        tglex.CashtagToken('$USD'),
    ),
    (
        '/start@jobs_bot',
        tglex.MessageEntityType.BOT_COMMAND,
        tglex.BotCommandToken('/start@jobs_bot'),
    ),
    (
        'https://telegram.org',
        tglex.MessageEntityType.URL,
        tglex.URLToken('https://telegram.org'),
    ),
    (
        'user@example.org',
        tglex.MessageEntityType.EMAIL,
        tglex.EmailToken('user@example.org'),
    ),
])
def test_single_token(text, entity_type, expected_token):
    """Test messages with a single token."""
    if entity_type is None:
        entities = []
    else:
        entities = [tglex.MessageEntity(
            type=entity_type,
            offset=0,
            length=len(text),
            user=None,
        )]
    msg = dataclasses.replace(BASE_MESSAGE, text=text, entities=entities)
    assert list(tglex.tokenize(msg)) == [expected_token]


def test_unknown_entity_type():
    """Test skipping entities with unknown types."""
    text = 'ok bad ok'
    entities = [tglex.MessageEntity(
        type=object(),
        offset=3,  # offset of word 'bad'
        length=len('bad'),
        user=None,
    )]
    msg = dataclasses.replace(BASE_MESSAGE, entities=entities, text=text)
    assert list(tglex.tokenize(msg)) == [tglex.Token('ok'), tglex.Token('ok')]


def test_entity_with_text_before():
    """Test text when special entity preceded by usual text."""
    usual_text = 'usual'
    email_text = 'user@example.org'
    text = '{} {}'.format(usual_text, email_text)
    entities = [tglex.MessageEntity(
        type=tglex.MessageEntityType.EMAIL,
        offset=len(usual_text) + 1,
        length=len(email_text),
        user=None,
    )]
    msg = dataclasses.replace(BASE_MESSAGE, text=text, entities=entities)
    assert list(tglex.tokenize(msg)) == [
        tglex.Token(usual_text),
        tglex.EmailToken(email_text),
    ]


def test_entity_with_text_after():
    """Test text when special entity followed by usual text."""
    email_text = 'user@example.org'
    usual_text = 'usual'
    text = '{} {}'.format(email_text, usual_text)
    entities = [tglex.MessageEntity(
        type=tglex.MessageEntityType.EMAIL,
        offset=0,
        length=len(email_text),
        user=None,
    )]
    msg = dataclasses.replace(BASE_MESSAGE, text=text, entities=entities)
    assert list(tglex.tokenize(msg)) == [
        tglex.EmailToken(email_text),
        tglex.Token(usual_text),
    ]


@pytest.mark.parametrize('text,expected_tokens', [
    (
        'hello world',
        [tglex.Token('hello'), tglex.Token('world')],
    ),
    (
        'hello, world',
        [tglex.Token('hello'), tglex.CommaToken(','), tglex.Token('world')],
    ),
    (
        'hello world!',
        [tglex.Token('hello'), tglex.Token('world'), tglex.DotToken('!')],
    ),
    ('hello?', [tglex.Token('hello'), tglex.QuestionToken('?')]),
    ('hello;', [tglex.Token('hello'), tglex.DotToken(';')]),
    ('hello\1', [tglex.Token('hello'), tglex.DotToken('\1')]),
])
def test_tokenize_usual_text(text, expected_tokens):
    assert list(tokenize_usual_text(text)) == expected_tokens
