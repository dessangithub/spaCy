from ...attrs import LIKE_NUM

# Thirteen, fifteen etc. are written separate: on üç

_num_words = [
    "bir",
    "iki",
    "üç",
    "dört",
    "bäş",
    "alty",
    "ýedi",
    "sekiz",
    "dokuz",
    "on",
    "ýigrimi",
    "otuz",
    "kyrk",
    "elli",
    "altmyş",
    "ýetmiş",
    "segsen",
    "togsan",
    "ýüz",
    "müň",
    "million",
    "milliard",
    "trillion",
    "kwadrillion",
    "kwintillion",
]


_ordinal_words = [
    "birinji",
    "ikinji",
    "üçünji",
    "dördünji",
    "bäşinji",
    "altynjy",
    "ýedinji",
    "sekizinji",
    "dokuzynjy",
    "onunjy",
    "ýigriminji",
    "otuzynjy",
    "kyrkynjy",
    "ellinji",
    "altmyşynjy",
    "ýetmişinji",
    "segseninji",
    "togsanynjy",
    "ýüzünji",
    "müňünji",
    "millionynjy",
    "milliardynjy" "trillionynjy",
    "kwadrillionynjy",
    "kwintillionynjy",
]

_ordinal_endings = ("inji", "nji", "ünjü")


def like_num(text):
    if text.startswith(("+", "-", "±", "~")):
        text = text[1:]
    text = text.replace(",", "").replace(".", "")
    if text.isdigit():
        return True
    if text.count("/") == 1:
        num, denom = text.split("/")
        if num.isdigit() and denom.isdigit():
            return True
    text_lower = text.lower()
    # Check cardinal number
    if text_lower in _num_words:
        return True
    # Check ordinal number
    if text_lower in _ordinal_words:
        return True
    if text_lower.endswith(_ordinal_endings):
        if text_lower[:-3].isdigit() or text_lower[:-4].isdigit():
            return True
    return False


LEX_ATTRS = {LIKE_NUM: like_num}
