"""Зогсоолын хүлээлгийн дараалал (US-07, ФШ-12).

Хүсэлтүүд зөвхөн ирсэн цагаараа жагсана. Өмнө зогсоол түрээсэлсэн эсэх эрэмбэд
нөлөөлөхгүй. Дарааллын дугаарыг хадгалахгүй, эрэмбэлж гаргана.
"""
from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class RentalRequest:
    """Хүлээгдэж буй зогсоолын түрээсийн хүсэлт."""
    request_id: str
    requested_at: datetime


def order_queue(requests):
    """Хүсэлтүүдийг ирсэн цагаар нь эрэмбэлж шинэ жагсаалт буцаана."""
    return sorted(requests, key=lambda r: r.requested_at)


def position(requests, request_id):
    """Хүсэлтийн дарааллын дугаар, 1-ээс эхэлнэ (US-07)."""
    for n, r in enumerate(order_queue(requests), start=1):
        if r.request_id == request_id:
            return n
    raise ValueError(f"хүсэлт олдсонгүй: {request_id}")
