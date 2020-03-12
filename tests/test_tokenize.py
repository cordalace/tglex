import datetime

import tglex


def test_tokenize():
    msg = tglex.Message(
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
        text='Hello world',
    )
    assert tglex.tokenize(msg) == [
        tglex.Token(text='Hello'),
        tglex.Token(text='world'),
    ]
