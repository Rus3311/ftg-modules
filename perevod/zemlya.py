import random
import logging
from .. import loader, utils
logger = logging.getLogger(__name__)

def register(cb):
    cb(jonytor())

class ArtsMod(loader.Module):
    """Юникод арты"""
    strings = {'name': 'фигня Jonytor'}

      async def fcmd(self, message):
        """Используй .jonytor с:"""
        args = utils.get_args_raw(message)
        if not args:
            r = random.randint(0, 5)
            logger.debug(r)
            if r == 0:
                await utils.answer(message, "┏━━━┓\n┃┏━━┛\n┃┗━━┓\n┃┏━━┛\n┃┃\n┗┛")
            elif r == 1:
                await utils.answer(message, "╭━━━╮\n┃╭━━╯\n┃╰━━╮\n┃╭━━╯\n┃┃\n╰╯")
            elif r == 2:
                await utils.answer(message, "🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕\n"
                                            "🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕\n"
                                            "🌕🌕🌗🌑🌑🌑🌑🌑🌓🌕🌕\n"
                                            "🌕🌕🌗🌑🌑🌑🌑🌑🌓🌕🌕\n"
                                            "🌕🌕🌗🌑🌕🌕🌕🌕🌓🌕🌕\n"
                                            "🌕🌕🌗🌑🌕🌕🌕🌕🌕🌕🌕\n"
                                            "🌕🌕🌗🌑🌑🌑🌑🌑🌓🌕🌕\n"
                                            "🌕🌕🌗🌑🌑🌑🌑🌑🌓🌕🌕\n"
                                            "🌕🌕🌕🌕🌕🌕🌕🌑🌓🌕🌕\n"
                                            "🌕🌕🌗🌕🌕🌕🌕🌑🌓🌕🌕\n"
                                            "🌕🌕🌗🌑🌑🌑🌑🌑🌓🌕🌕\n"
                                            "🌕🌕🌗🌑🌑🌑🌑🌑🌓🌕🌕\n"
                                            "🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕\n"
                                            "🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕")
            elif r == 3:
                await utils.answer(message, "🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕\n"
                                            "🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕\n"
                                            "🌕🌕🌗🌑🌑🌑🌑🌑🌓🌕🌕\n"
                                            "🌕🌕🌗🌑🌑🌑🌑🌑🌕🌕🌕\n"
                                            "🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕\n"
                                            "🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕\n"
                                            "🌕🌕🌗🌑🌑🌑🌑🌓🌕🌕🌕\n"
                                            "🌕🌕🌗🌑🌑🌑🌑🌕🌕🌕🌕\n"
                                            "🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕\n"
                                            "🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕\n"
                                            "🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕\n"
                                            "🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕\n"
                                            "🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕")
            elif r == 4:
                await utils.answer(message,"🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕/n"
                                           "🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕/n"
                                           "🌕🌕🌕🌕🌕🌗🌑🌑🌓🌕🌕/n"
                                           "🌕🌕🌕🌕🌕🌗🌑🌑🌓🌕🌕/n"
                                           "🌕🌕🌕🌕🌕🌗🌑🌑🌓🌕🌕/n"
                                           "🌕🌕🌕🌕🌕🌗🌑🌑🌓🌕🌕/n"
                                           "🌕🌕🌕🌕🌕🌗🌑🌑🌓🌕🌕/n"
                                           "🌕🌕🌕🌕🌕🌗🌑🌑🌓🌕🌕/n"
                                           "🌕🌕🌕🌕🌕🌗🌑🌑🌓🌕🌕/n"
                                           "🌕🌗🌑🌑🌓🌗🌑🌑🌓🌕🌕/n"
                                           "🌕🌗🌑🌑🌓🌗🌑🌑🌓🌕🌕/n"
                                           "🌕🌗🌑🌑🌑🌑🌑🌑🌓🌕🌕/n"
                                           "🌕🌗🌑🌑🌑🌑🌑🌑🌓🌕🌕/n"
                                           "🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕/n"
                                           "🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕")
