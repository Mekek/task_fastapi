import pytest
from datetime import datetime
from app import calculate_deposit

@pytest.mark.parametrize(
    "date, periods, amount, rate, expected_result",
    [
        ("31.01.2021", 3, 10000, 6, {
            "31.01.2021": 10050.0,
            "28.02.2021": 10100.25,
            "31.03.2021": 10150.75
        }),
        ("29.01.2021", 6, 15000, 5, {
            "29.01.2021": 15062.5,
            "28.02.2021": 15125.26,
            "29.03.2021": 15188.28,
            "29.04.2021": 15251.57,
            "29.05.2021": 15315.12,
            "29.06.2021": 15378.93
        }),
        ("01.01.2021", 3, 20000, 7, {
            "01.01.2021": 20116.67,
            "01.02.2021": 20234.01,
            "01.03.2021": 20352.05
        })
    ]
)
def test_calculate_deposit(date, periods, amount, rate, expected_result):
    result = calculate_deposit(date, periods, amount, rate)
    assert result == expected_result

