from shobdohash import ShobdoHash


def test_basics():
    s = ShobdoHash()

    assert s('সরিশা') == s('শরিষা')
    assert s('যজ্ঞ') == s('জজ্ঞ')


def test_za_fola():
    s = ShobdoHash()

    assert s('কাব্য') == s('কাব্ব')
    assert s('কাব্যগ্রন্থ') == s('কাব্বগ্রন্থ')


def test_ba_fola():
    s = ShobdoHash()

    assert s('ক্বারি') == s('কারি')
