from unittest.mock import call

import pytest

from lr2d.data.preprocessing_helpers import convert_to_int, row_to_list, preprocess


@pytest.fixture
def raw_and_clean_data_file(tmpdir):
    """Auxiliar function to create a raw and clean data file for testing"""
    raw_path = tmpdir.join("raw.txt")
    clean_path = tmpdir.join("clean.txt")
    with open(raw_path, "w") as f:
        f.write("1,801\t201,411\n"
                "1,767565,112\n"
                "2,002\t333,209\n"
                "1990\t782,911\n"
                "1,285\t389129\n"
                )
    return raw_path, clean_path


def row_to_list_bug_free(row):
    return_values = {"1,801\t201,411\n": ["1,801", "201,411"],
                     "1,767565,112\n": None,
                     "2,002\t333,209\n": ["2,002", "333,209"],
                     "1990\t782,911\n": ["1990", "782,911"],
                     "1,285\t389129\n": ["1,285", "389129"],
                     }
    return return_values[row]


def convert_to_int_bug_free(comma_separated_integer_string):
    return_values = {"1,801": 1801,
                     "201,411": 201411,
                     "2,002": 2002,
                     "333,209": 333209,
                     "1990": None,
                     "782,911": 782911,
                     "1,285": 1285,
                     "389129": None,
                     }
    return return_values[comma_separated_integer_string]


class TestConvertToInt(object):
    """Test the convert_to_int function
        Differente test cases: Bug free, no comma, one comma, two commas,
        incorrectly placed comma, missing comma, float valued string.
    """

    def test_with_no_comma(self):
        test_argument = "756"
        expected = 756
        actual = convert_to_int(test_argument)
        assert actual == expected, "Expected: 756, Actual: {0}".format(actual)

    def test_with_one_comma(self):
        test_argument = "2,081"
        expected = 2081
        actual = convert_to_int(test_argument)
        assert actual == expected, "Expected: 2081, Actual: {0}".format(actual)

    def test_with_two_commas(self):
        test_argument = "1,034,891"
        expected = 1034891
        actual = convert_to_int(test_argument)
        assert actual == expected, "Expected: 1034891, Actual: {0}".format(
            actual)

    def test_string_with_incorrectly_placed_comma(self):
        test_argument = "12,72,891"
        expected = None
        actual = convert_to_int(test_argument)
        assert actual == expected, "Expected: None, Actual: {0}".format(actual)

    def test_string_with_missing_comma(self):
        test_argument = "178100,301"
        expected = None
        actual = convert_to_int(test_argument)
        assert actual == expected, "Expected: None, Actual: {0}".format(actual)

    def test_float_valued_string(self):
        test_argument = "6.9"
        expected = None
        actual = convert_to_int(test_argument)
        assert actual == expected, "Expected: None, Actual: {0}".format(actual)


class TestRowToList(object):
    """ Test the row_to_list function
        Differente test cases: Bug free, one tab, two tabs, no tab.
    """

    def test_no_tab_no_missing_value(self):
        actual = row_to_list("123\n")
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    def test_two_tabs_no_missing_value(self):
        actual = row_to_list("123\t4,567\t89\n")
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    def test_one_tab_with_missing_value(self):
        actual = row_to_list("\t4,567\n")
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    def test_no_tab_with_missing_value(self):
        actual = row_to_list("\n")
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    def test_two_tabs_with_missing_value(self):
        actual = row_to_list("123\t\t89\n")
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    def test_normal_argument_1(self):
        actual = row_to_list("123\t4,567\n")
        expected = ["123", "4,567"]
        assert actual == expected, "Expected: {0}, Actual: {1}".format(
            expected, actual)

    def test_normal_argument_2(self):
        actual = row_to_list("1,059\t186,606\n")
        expected = ["1,059", "186,606"]
        assert actual == expected, "Expected: {0}, Actual: {1}".format(
            expected, actual)


# @pytest.mark.xfail(reason="This test is expected to fail until the mocker.patch is fixed")
class TestPreprocess(object):
    """Test the Preprocess packege using mock objects"""

    def test_raw_data(self, raw_and_clean_data_file, mocker):
        raw_path, clean_path = raw_and_clean_data_file
        row_to_list_mock = mocker.patch(
            "lr2d.data.preprocessing_helpers.row_to_list", side_effect=row_to_list_bug_free)
        convert_to_int_mock = mocker.patch("lr2d.data.preprocessing_helpers.convert_to_int",
                                           side_effect=convert_to_int_bug_free
                                           )
        preprocess(raw_path, clean_path)
        assert row_to_list_mock.call_args_list == [call("1,801\t201,411\n"),
                                                   call("1,767565,112\n"),
                                                   call("2,002\t333,209\n"),
                                                   call("1990\t782,911\n"),
                                                   call("1,285\t389129\n")
                                                   ]
        assert convert_to_int_mock.call_args_list == [call("1,801"), call("201,411"), call("2,002"), call("333,209"),
                                                      call("1990"),  call("782,911"), call(
                                                          "1,285"), call("389129")
                                                      ]
        with open(clean_path, "r") as f:
            lines = f.readlines()
        first_line = lines[0]
        assert first_line == "1801\t201411\n"
        second_line = lines[1]
        assert second_line == "2002\t333209\n"
