import re

# 4 цифр + (заавал биш хоосон зай) + 3 кирилл том үсэг (Ө, Ү орно)
_PLATE_RE = re.compile(r"^(\d{4})\s?([А-ЯЁӨҮ]{3})$")


def normalize_plate(plate: str) -> str:
    """Оруулсан утгыг цэвэрлэнэ: илүү зайг авч, том үсэг болгоно."""
    if not isinstance(plate, str):
        raise TypeError("Дугаар string байх ёстой")
    return " ".join(plate.strip().upper().split())


def is_valid_plate(plate: str) -> bool:
    """Монгол машины дугаар зөв эсэхийг шалгана.

    Зөв:   '1234 УБА', '1234УБА', ' 1234 убв '
    Буруу: '123 УБА', '1234 UBA', '12345 УБА', '1234 УБ'
    """
    try:
        value = normalize_plate(plate)
    except TypeError:
        return False
    return bool(_PLATE_RE.match(value))


def format_plate(plate: str) -> str:
    """Зөв дугаарыг '1234 УБА' гэсэн нэг хэлбэрт оруулна. Буруу бол ValueError өгнө."""
    value = normalize_plate(plate)
    m = _PLATE_RE.match(value)
    if not m:
        raise ValueError(f"Машины дугаар буруу байна: {plate!r}")
    return f"{m.group(1)} {m.group(2)}"


if __name__ == "__main__":
    tests = ["1234 УБА", "1234убв", "  5678  ӨВА ", "123 УБА", "1234 UBA", "12345 УБА", ""]
    for t in tests:
        print(f"{t!r:16} -> {is_valid_plate(t)}")
