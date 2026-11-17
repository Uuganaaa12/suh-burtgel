"""Машины улсын дугаарыг шалгаж нэг хэлбэрт оруулна (US-04, Лаб 12).

Анхны хувилбарыг AI (Claude Code) бичсэн. Review хийж хоёр засвар оруулав
(docs/lab12.md, 4-р хэсэг):

1. Хоосон зайг зөвхөн ASCII зайгаар биш, Unicode-ийн бүх хоосон зайгаар
   (таб, NBSP) таслав. Утаснаас хуулж буулгасан дугаар татгалзагдахгүй.
2. Үсгийг `upper()` хийхээс өмнө зөвшөөрөгдсөн 35 үсгийн жагсаалттай тулгав.
   Ингэснээр «ᲀ» (U+1C80) зэрэг хуучин кирилл үсэг «В» болж хувирахгүй.
"""
import re

MAX_RAW_LENGTH = 20
UPPER = "АБВГДЕЁЖЗИЙКЛМНОӨПРСТУҮФХЦЧШЩЪЫЬЭЮЯ"     # монгол кирилл 35 үсэг
LETTERS = UPPER + UPPER.lower()

# \d биш [0-9]: \d нь «０», «٠» зэрэг ASCII бус цифрийг ч зөвшөөрдөг.
PLATE_RE = re.compile(rf"([0-9]{{4}}) ?([{LETTERS}]{{3}})")


def normalize_plate(raw: str) -> str:
    """«0123уба», « 0123  УБА » зэрэг оролтыг «0123 УБА» болгоно.

    Хэлбэр буруу бол ValueError, str биш бол TypeError шиднэ.
    """
    if not isinstance(raw, str):
        raise TypeError(f"Улсын дугаар текст (str) байх ёстой, {type(raw).__name__} төрөл ирлээ.")
    if len(raw) > MAX_RAW_LENGTH:
        raise ValueError(f"Улсын дугаар {MAX_RAW_LENGTH} тэмдэгтээс урт байж болохгүй.")

    match = PLATE_RE.fullmatch(" ".join(raw.split()))
    if match is None:
        if any(ch.isascii() and ch.isalpha() for ch in raw):
            raise ValueError("Улсын дугаарт латин үсэг орсон байна. Зөвхөн кирилл үсэг ашиглана уу.")
        if any(ch.isdigit() and not ch.isascii() for ch in raw):
            raise ValueError("Улсын дугаарт стандарт бус цифр орсон байна. Зөвхөн 0-9 цифр ашиглана уу.")
        raise ValueError("Улсын дугаарын хэлбэр буруу байна. 4 цифр, 3 кирилл үсэгтэй байх ёстой, "
                         "жишээ нь «0123 УБА».")

    digits, letters = match.groups()
    return f"{digits} {letters.upper()}"
