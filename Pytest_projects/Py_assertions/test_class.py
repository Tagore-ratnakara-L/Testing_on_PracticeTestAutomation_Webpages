class Test_My_Stuff():
    # def test_a1(self):
    #     assert 4 < 5
    #
    # def test_a2(self):
    #     assert 1
    #
    # def test_a3(self):
    #     assert "abc" in 'abcd'
    #
    # def test_a4(self):
    #     assert ((3 - 4) * (4 / 1)) != 4
    #
    # def test_a5(self):
    #     assert 6 not in divmod(10, 2)
    #     assert 'put' not in "This is a fail sample"

    def test_type(self):
        assert type(1) == int

    def test_strs(self):
        assert str.upper('python') == 'PYTHON'
        assert 'pytest'.capitalize() == 'Pytest'
