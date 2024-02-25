def test_a1():
    assert 4 < 5


def test_a2():
    assert 1


def test_a3():
    assert "abc" in 'abcd'


def test_a4():
    assert ((3 - 4) * (4 / 1)) != 4


def test_a5():
    assert 6 not in divmod(10, 2)
    assert 'put' not in "This is a fail sample"

