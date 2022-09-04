from git_log_analysis.utils.file_system import is_allowed_file


class TestFileSystem:
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def test_should_true_log_when_is_allowed_file(self):
        # given
        input_file_name = "abc/def/test.py"
        allowed_extension = ["py"]
        expected_result = True

        # when
        test_result = is_allowed_file(input_file_name, allowed_extension)

        # then
        assert expected_result == test_result

    def test_should_false_log_when_is_allowed_file(self):
        # given
        input_file_name = "abc/def/test.py"
        allowed_extension = ["java"]
        expected_result = False

        # when
        test_result = is_allowed_file(input_file_name, allowed_extension)

        # then
        assert expected_result == test_result
