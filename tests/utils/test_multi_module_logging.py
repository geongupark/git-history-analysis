from git_log_analysis.utils.multi_module_logging import MultiModuleLogger
import logging
import logging.handlers


class TestMultiModuleLogger:
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def test_should_have_logger_name_log_when_create_logger(self):
        # given
        test_logger_name = "TestLogger"
        expected_result = set([test_logger_name])

        # when
        test_logger = MultiModuleLogger.create_logger(test_logger_name)

        # then
        assert expected_result == MultiModuleLogger.logger_names

    def test_should_debug_logging_mode_log_when_create_logger(self):
        # given
        test_logger_name = "TestLogger"
        expected_result = logging.DEBUG

        # when
        test_logger = MultiModuleLogger.create_logger(test_logger_name)

        # then
        assert expected_result == MultiModuleLogger.logging_modes[test_logger_name]

    def test_should_not_have_name_log_when_set_logging_mode(self):
        # given
        test_logger_name = "TestLogger"
        expected_result = logging.INFO
        test_logger = MultiModuleLogger.create_logger(test_logger_name)

        # when
        MultiModuleLogger.set_logging_mode(logging.INFO, test_logger_name)

        # then
        assert expected_result == MultiModuleLogger.logging_modes[test_logger_name]
