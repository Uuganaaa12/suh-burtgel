"""Сарын нэхэмжлэхийн нийт дүн (US-12, US-13).

Нийт дүн = СӨХ-ийн хураамж + зогсоолын түрээс + алданги. Алдангийг
`late_fee()` тооцно. `amount_due()` нэхэмжлэхийг өгөгдлийн сангаас уншдаг тул
тестэд repository-г mock-оор орлуулна.
"""
from datetime import date
from decimal import Decimal

from suh.late_fee import late_fee


def invoice_total(fee: int, rent: int, days_overdue: int, daily_rate: Decimal) -> int:
    """Хураамж, түрээс, алдангийн нийлбэрийг бүхэл төгрөгөөр буцаана."""
    if fee < 0 or rent < 0:
        raise ValueError("хураамж, түрээс сөрөг байж болохгүй")
    unpaid = fee + rent
    return unpaid + late_fee(unpaid, days_overdue, daily_rate)


def amount_due(invoice_id: int, repo, today: date, daily_rate: Decimal) -> int:
    """Нэхэмжлэхийг repository-оос уншиж, өнөөдрийн байдлаар төлөх дүнг буцаана."""
    invoice = repo.get_invoice(invoice_id)
    if invoice is None:
        raise LookupError(f"нэхэмжлэх олдсонгүй: {invoice_id}")
    if invoice["paid"]:
        return 0
    days_overdue = (today - invoice["due_date"]).days
    return invoice_total(invoice["fee"], invoice["rent"], days_overdue, daily_rate)
