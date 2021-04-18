

from tests.functional import check

startMessage = """
Hi!

My name is @UnitConversionBot. I can convert from one unit to another.
Just type something like "100 ft to m" (in private chat with me) or "/convert 1 km2 to m2" (in group chats). For more info type /help

If you have an issue or just want to say thanks, feel free to contact my master @kirillmaltsev or rate me at https://storebot.me/bot/unitconversionbot
Thank you for chatting with me :-)
""".strip()


def test_start():
    check(
        startMessage,
        text='/start',
    )
