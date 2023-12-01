from day01 import get_calibration_value


class TestDay01:

    def test_get_calibration_value_sdsds(self):
        assert get_calibration_value('x1x3x') == 13

    def test_get_calibration_value_ddd(self):
        assert get_calibration_value('125') == 15

    def test_get_calibration_value_dd(self):
        assert get_calibration_value('12') == 12

    def test_get_calibration_value_d(self):
        assert get_calibration_value('8') == 88

    def test_get_calibration_value_dssd(self):
        assert get_calibration_value('8xx9') == 89
