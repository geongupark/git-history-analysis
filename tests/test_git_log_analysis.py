#!/usr/bin/env python

"""Tests for `git_log_analysis` package."""
import subprocess
from git_log_analysis.git_log_analyzer import get_count_by_files, get_git_log_result


class TestGitLogAnalyzer:
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def test_should_valid_counts_log_when_get_count_by_files(self):
        # given
        input_git_log_results = ["M\tsrc/car/handle.py", "M\tsrc/car/body.py", "A\tsrc/car/handle.py",
                                 "D\tsrc/car/body.py", "M\tsrc/car/body.py", "R50a\tsrc/car/side.py src/car/side_mirror.py",
                                 "A\tsrc/car/handle.py"]
        expected_result = {"src/car/handle.py": 3,
                           "src/car/side_mirror.py": 1, "src/car/body.py": 1}

        # when
        test_result = get_count_by_files(input_git_log_results)

        # then
        assert expected_result == test_result

    def test_should_valid_result_log_when_get_git_log_result(self, mocker):
        # given
        counts_by_files = {"src/car/handle.py": 3, "src/car/config.json": 2,
                           "src/car/side_mirror.py": 1, "src/car/body.py": 1}
        real_files = ["./src/car/handle.py",
                      "./src/car/side_mirror.py", "src/car/body.py"]
        input_process = subprocess.CompletedProcess(
            args="echo", returncode=0, stdout="abcd\nefgh\nbye")

        mocker.patch(
            "git_log_analysis.git_log_analyzer.subprocess.run", return_value=input_process)
        mocker.patch(
            "git_log_analysis.git_log_analyzer.get_count_by_files", return_value=counts_by_files)
        mocker.patch(
            "git_log_analysis.git_log_analyzer.traversing_dir_for_file", return_value=real_files)
        expected_result = {"src/car/handle.py": 3,
                           "src/car/side_mirror.py": 1, "src/car/body.py": 1}
        # when
        test_result = get_git_log_result("./")

        # then
        assert expected_result == test_result
