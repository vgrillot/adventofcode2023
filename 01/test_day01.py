from day01 import get_calibration_value, rename_numbers, compute_value_from_file


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

    def test_rename_numbers_one(self):
        assert rename_numbers('one') == '1'

    def test_rename_numbers_oneone(self):
        assert rename_numbers('oneone') == '11'

    def test_rename_numbers_one1one(self):
        assert rename_numbers('one1one') == '111'

    def test_rename_numbers_eightwothree(self):
        assert rename_numbers('eightwothree') == '83'

    def test_rename_numbers_two1nine(self):
        assert rename_numbers('two1nine') == '219'

    def test_rename_numbers_and_calc_value(self):
        values = [
            ('two1nine', 29),
            ('eightwothree', 83),
            ('abcone2threexyz', 13),
            ('xtwone3four', 24),
            ('4nineeightseven2', 42),
            ('zoneight234', 14),
            ('7pqrstsixteen', 76)]
        for txt, expected_value in values:
            assert get_calibration_value(rename_numbers(txt)) == expected_value

    def test_file(self):
        assert compute_value_from_file('test_file') == 281
