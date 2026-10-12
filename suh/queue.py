"""Зогсоолын хүлээлгийн дараалал (US-09).

Нэг дэх машины хүсэлт нэмэлт машиныхаас түрүүлнэ. Ижил ангиллынх хүсэлт
гаргасан цагаараа жагсана. Дарааллын дугаарыг хадгалахгүй, эрэмбэлж гаргана.
"""
from dataclasses import dataclass
from datetime import datetime

FIRST_CAR = "нэг дэх"
EXTRA_CAR = "нэмэлт"
_RANK = {FIRST_CAR: 0, EXTRA_CAR: 1}


@dataclass(frozen=True)
class RentalRequest:
    """Хүлээгдэж буй зогсоолын түрээсийн хүсэлт."""
    request_id: str
    category: str
    requested_at: datetime


def classify(active_rentals: int) -> str:
    """Сууц идэвхтэй түрээсгүй бол нэг дэх, байвал нэмэлт машины хүсэлт (UC-05, 3-р алхам)."""
    if active_rentals < 0:
        raise ValueError("идэвхтэй түрээсийн тоо сөрөг байж болохгүй")
    return FIRST_CAR if active_rentals == 0 else EXTRA_CAR


def order_queue(requests):
    """Хүсэлтүүдийг дарааллын журмаар эрэмбэлж шинэ жагсаалт буцаана."""
    for r in requests:
        if r.category not in _RANK:
            raise ValueError(f"тодорхойгүй ангилал: {r.category}")
    return sorted(requests, key=lambda r: (_RANK[r.category], r.requested_at))
