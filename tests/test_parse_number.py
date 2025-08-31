import pytest
import sys
import os

from parsers.integer_parser import parse_number


def test_parse_number():
    assert parse_number("123abc", 0) == (123, 3)
    assert parse_number("45.67,rest", 0) == (45.67, 5)
    assert parse_number("-89xyz", 0) == (-89, 3)
    assert parse_number("12.34.56", 0) == (12.34, 5)
    assert parse_number("0.5gm", 0) == (0.5, 3)
    assert parse_number("0K", 0) == (0, 1)
    assert parse_number("1e+10cells", 0) == (1e10, 5)
    assert parse_number("1e-10meter", 0) == (1e-10, 5)
    with pytest.raises(ValueError):
        parse_number("+ABCDEF", 0)
    with pytest.raises(ValueError):
        parse_number(".ABCDEF", 0)
    with pytest.raises(ValueError):
        parse_number("000123", 0)
