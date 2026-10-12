"""Хугацаа хэтэрсэн нэхэмжлэхийн алданги (US-13).

Иргэний хуулийн 232.6: алданги хоногт 0.5%-иас ихгүй. 232.4: нийт дүн нь
төлөгдөөгүй дүнгийн 50%-иас хэтрэхгүй. Хувийг тохиргооны файлаас уншина.
0% бол СӨХ алданги авахгүй.
"""
from decimal import ROUND_HALF_UP, Decimal

MAX_DAILY_RATE = Decimal("0.005")
MAX_SHARE = Decimal("0.5")


def late_fee(unpaid: int, days_overdue: int, daily_rate: Decimal) -> int:
    """Алдангийг бүхэл төгрөгөөр буцаана."""
    if not Decimal(0) <= daily_rate <= MAX_DAILY_RATE:
        raise ValueError("алдангийн хувь хоногт 0–0.5% байна (Иргэний хууль 232.6)")
    if unpaid < 0:
        raise ValueError("төлөгдөөгүй дүн сөрөг байж болохгүй")
    if days_overdue <= 0:
        return 0
    fee = min(Decimal(unpaid) * daily_rate * days_overdue, Decimal(unpaid) * MAX_SHARE)
    return int(fee.quantize(Decimal(1), rounding=ROUND_HALF_UP))
