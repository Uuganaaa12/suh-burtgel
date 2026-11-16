"""Алдангийн тооцооны тест (US-13, Иргэний хуулийн 232.4, 232.6)."""
from decimal import Decimal

import pytest

from suh.late_fee import late_fee

RATE = Decimal("0.005")


def test_seven_days_overdue():
    assert late_fee(100_000, 7, RATE) == 3_500


def test_total_is_capped_at_half_of_unpaid():
    # 150 хоног × 0.5% = 75%, гэвч хуулиар 50%-иас хэтрэхгүй.
    assert late_fee(100_000, 150, RATE) == 50_000


@pytest.mark.parametrize("days", [0, -3])
def test_no_fee_when_not_overdue(days):
    assert late_fee(100_000, days, RATE) == 0


def test_zero_rate_means_no_fee():
    assert late_fee(100_000, 30, Decimal(0)) == 0


def test_result_is_rounded_to_whole_togrog():
    assert late_fee(107_100, 3, Decimal("0.001")) == 321


@pytest.mark.parametrize("rate", [Decimal("0.01"), Decimal("-0.001")])
def test_rate_outside_legal_range_is_rejected(rate):
    with pytest.raises(ValueError):
        late_fee(100_000, 7, rate)


def test_negative_unpaid_is_rejected():
    with pytest.raises(ValueError):
        late_fee(-1, 7, RATE)
