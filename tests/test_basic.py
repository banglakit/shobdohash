from shobdohash import ShobdoHash

s = ShobdoHash()


def test_basics():
    assert s('সরিশা') == s('শরিষা')
    assert s('যজ্ঞ') == s('জজ্ঞ')


def test_za_fola():
    assert s('কাব্য') == s('কাব্ব')
    assert s('কাব্যগ্রন্থ') == s('কাব্বগ্রন্থ')


def test_ba_fola():
    assert s('ক্বারি') == s('কারি')


def test_ng_fola():
    assert s('যজ্ঞ') == s('জগগ')


def test_khiyo():
    assert s('ক্ষয়') == s('খয়')