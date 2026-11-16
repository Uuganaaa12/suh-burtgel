"""Лаб 10: invoice_total(), amount_due() тест. Тест бүр Arrange-Act-Assert бүтэцтэй."""
from datetime import date
from decimal import Decimal
from unittest.mock import Mock

import pytest

from suh.billing import amount_due, invoice_total

RATE = Decimal("0.005")          # хоногт 0.5% (Иргэний хуулийн дээд хязгаар)


# ---- хэвийн тохиолдол
def test_total_on_time_is_fee_plus_rent():
    # Arrange
    fee, rent = 45_000, 60_000
    # Act
    total = invoice_total(fee, rent, days_overdue=0, daily_rate=RATE)
    # Assert
    assert total == 105_000


def test_total_with_seven_days_late_fee():
    # Arrange: 100,000₮ × 0.5% × 7 хоног = 3,500₮ алданги
    fee, rent = 40_000, 60_000
    # Act
    total = invoice_total(fee, rent, days_overdue=7, daily_rate=RATE)
    # Assert
    assert total == 103_500


# ---- хилийн тохиолдол
def test_zero_fee_and_rent_gives_zero():
    # Arrange
    fee, rent = 0, 0
    # Act
    total = invoice_total(fee, rent, days_overdue=30, daily_rate=RATE)
    # Assert
    assert total == 0


@pytest.mark.parametrize("fee, rent", [(-1, 60_000), (45_000, -5)])
def test_negative_amount_is_rejected(fee, rent):
    # Arrange: сөрөг дүн
    # Act, Assert
    with pytest.raises(ValueError):
        invoice_total(fee, rent, days_overdue=0, daily_rate=RATE)


def test_very_late_fee_is_capped_at_half():
    # Arrange: 10 жил хэтэрсэн ч алданги 50%-иас хэтрэхгүй
    fee, rent = 1_000_000_000, 0
    # Act
    total = invoice_total(fee, rent, days_overdue=3650, daily_rate=RATE)
    # Assert
    assert total == 1_500_000_000


# ---- mock: өгөгдлийн санг орлуулна
def test_amount_due_reads_invoice_from_repository():
    # Arrange: жинхэнэ өгөгдлийн сангийн оронд mock
    repo = Mock()
    repo.get_invoice.return_value = {"fee": 40_000, "rent": 60_000, "paid": False,
                                     "due_date": date(2026, 11, 10)}
    # Act
    due = amount_due(7, repo, today=date(2026, 11, 17), daily_rate=RATE)
    # Assert
    assert due == 103_500
    repo.get_invoice.assert_called_once_with(7)
