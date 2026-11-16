from datetime import datetime

import pytest

from suh.queue import RentalRequest, order_queue, position


def req(request_id, month, day, hour=9):
    return RentalRequest(request_id, datetime(2026, month, day, hour))


def ids(requests):
    return [r.request_id for r in requests]


SAMPLE = [req("R1", 9, 1), req("R2", 9, 3), req("R3", 9, 2), req("R4", 8, 30)]


def test_ordered_by_request_date():
    # R1-ийн сууц өмнө нь зогсоол түрээсэлдэг ч эрэмбэд нөлөөлөхгүй, огноогоороо жагсана.
    assert ids(order_queue(SAMPLE)) == ["R4", "R1", "R3", "R2"]


def test_same_day_ordered_by_time():
    queue = [req("A", 9, 2, hour=15), req("B", 9, 2, hour=8)]
    assert ids(order_queue(queue)) == ["B", "A"]


def test_empty_queue():
    assert order_queue([]) == []


def test_input_list_is_not_changed():
    queue = [req("R2", 9, 3), req("R1", 9, 1)]
    order_queue(queue)
    assert ids(queue) == ["R2", "R1"]


@pytest.mark.parametrize("request_id, expected", [("R4", 1), ("R1", 2), ("R2", 4)])
def test_position(request_id, expected):
    assert position(SAMPLE, request_id) == expected


def test_unknown_request_is_rejected():
    with pytest.raises(ValueError):
        position(SAMPLE, "X")
