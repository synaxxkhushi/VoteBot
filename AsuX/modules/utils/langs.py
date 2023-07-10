from pyrogram.enums import ChatType
from pyrogram.types import CallbackQuery, InlineQuery, Message

from AsuX.db.lang_db import Langs
from strings import get_string


def lang(mystic):
    async def wrapper(_, message, **kwargs):
        if isinstance(message, CallbackQuery):
            chat = message.message.chat
        elif isinstance(message, Message):
            chat = message.chat
        elif isinstance(message, InlineQuery):
            chat, chat.type = message.from_user, ChatType.PRIVATE
        else:
            raise TypeError(f"Update type '{message.__name__}' is not supported.")
        try:
            language = Langs(chat.id).get_lang()
            language = get_string(language)
        except:
            language = get_string("en")
        return await mystic(_, message, language)

    return wrapper
