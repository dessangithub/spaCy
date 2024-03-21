from ...symbols import NORM, ORTH
from ...util import update_exc
from ..tokenizer_exceptions import BASE_EXCEPTIONS

_exc = {}

_abbrev_exc = [
    # Weekdays abbreviations
    {ORTH: "duş", NORM: "duşenbe"},
    {ORTH: "siş", NORM: "sişenbe"},
    {ORTH: "Çar", NORM: "Çarşenbe"},
    {ORTH: "pen", NORM: "penşenbe"},
    {ORTH: "ann", NORM: "anna"},
    {ORTH: "şen", NORM: "şenbe"},
    {ORTH: "ýek", NORM: "ýekşenbe"},
    # Months abbreviations
    {ORTH: "ýan", NORM: "ýanwar"},
    {ORTH: "few", NORM: "fewral"},
    {ORTH: "mar", NORM: "mart"},
    {ORTH: "apr", NORM: "aprel"},
    {ORTH: "maý", NORM: "maý"},
    {ORTH: "iýn", NORM: "iýun"},
    {ORTH: "iýl", NORM: "iýul"},
    {ORTH: "awg", NORM: "awgust"},
    {ORTH: "sen", NORM: "sentýabr"},
    {ORTH: "okt", NORM: "oktýabr"},
    {ORTH: "noý", NORM: "noýabr"},
    {ORTH: "dek", NORM: "dekabr"},
    # Number abbreviations
    {ORTH: "mlrd", NORM: "milliýard"},
    {ORTH: "mln", NORM: "milliýon"},
]

for abbr in _abbrev_exc:
    for orth in (abbr[ORTH], abbr[ORTH].capitalize(), abbr[ORTH].upper()):
        _exc[orth] = [{ORTH: orth, NORM: abbr[NORM]}]
        _exc[orth + "."] = [{ORTH: orth + ".", NORM: abbr[NORM]}]


TOKENIZER_EXCEPTIONS = update_exc(BASE_EXCEPTIONS, _exc)
