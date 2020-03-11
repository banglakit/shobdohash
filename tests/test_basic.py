from shobdohash import ShobdoHash


def test_basics():
    s = ShobdoHash()

    assert s('সরিশা') == s('শরিষা')
    assert s('যজ্ঞ') == s('জজ্ঞ')