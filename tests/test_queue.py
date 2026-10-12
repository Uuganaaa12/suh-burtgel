from datetime import datetime

import pytest

from suh.queue import EXTRA_CAR, FIRST_CAR, RentalRequest, classify, order_queue


def req(request_id, category, month, day, hour=9):
    return RentalRequest(request_id, category, datetime(2026, month, day, hour))


def ids(requests):
    return [r.request_id for r in requests]


def test_first_car_requests_come_before_extra_ones():
    # R4 хамгийн эрт хүссэн ч нэмэлт машин тул нэг дэх машинуудын ард орно.
    queue = [
        req("R1", EXTRA_CAR, 9, 1),
        req("R2", FIRST_CAR, 9, 3),
        req("R3", FIRST_CAR, 9, 2),
        req("R4", EXTRA_CAR, 8, 30),
    ]
    assert ids(order_queue(queue)) == ["R3", "R2", "R4", "R1"]


def test_same_category_same_day_ordered_by_time():
    queue = [req("A", FIRST_CAR, 9, 2, hour=15), req("B", FIRST_CAR, 9, 2, hour=8)]
    assert ids(order_queue(queue)) == ["B", "A"]


def test_empty_queue():
    assert order_queue([]) == []


def test_input_list_is_not_changed():
    queue = [req("R1", EXTRA_CAR, 9, 1), req("R2", FIRST_CAR, 9, 3)]
    order_queue(queue)
    assert ids(queue) == ["R1", "R2"]


def test_unknown_category_is_rejected():
    with pytest.raises(ValueError):
        order_queue([req("X", "хувийн", 9, 1)])


@pytest.mark.parametrize("active, expected", [(0, FIRST_CAR), (1, EXTRA_CAR), (2, EXTRA_CAR)])
def test_classify(active, expected):
    assert classify(active) == expected


def test_classify_rejects_negative_count():
    with pytest.raises(ValueError):
        classify(-1)
