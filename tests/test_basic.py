import pytest

from shobdohash import ShobdoHash

s = ShobdoHash()


def test_basics():
    assert s('সরিশা') == s('শরিষা')
    assert s('যজ্ঞ') == s('জজ্ঞ')


@pytest.mark.parametrize('one,two', [
    ('কাব্য', 'কাব্ব'),
    ('কাব্যগ্রন্থ', 'কাব্বগ্রন্থ'),
    ('বাহ্য', 'বাহহ')
])
def test_za_fola(one, two):
    assert s(one) == s(two)


@pytest.mark.parametrize('one,two', [
    ('পদ্ম', 'পদ্দ'),
    ('তন্ময়', 'তনময়'),
])
def test_ma_fola(one, two):
    assert s(one) == s(two)


def test_ba_fola():
    assert s('ক্বারি') == s('কারি')


def test_ng_fola():
    assert s('যজ্ঞ') == s('জগগ')


def test_khiyo():
    assert s('ক্ষয়') == s('খয়')
