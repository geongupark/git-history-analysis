"""Main module."""
import subprocess

from .utils.multi_module_logging import MultiModuleLogger
from .utils.file_system import traversing_dir_for_file

LOGGER = MultiModuleLogger.create_logger("gla")


def get_count_by_files(git_log_results: list):
    count_by_files = {}
    git_log_results.reverse()

    for result in git_log_results:
        if '\t' in result:
            split_result = result.split()
            if split_result[0] in ["M", "A"]:
                count_by_files[split_result[1]] = (
                    count_by_files[split_result[1]] + 1) if split_result[1] in count_by_files else 1
            elif split_result[0] in ["D"]:
                if split_result[1] in count_by_files:
                    del(count_by_files[split_result[1]])
            elif "R" in split_result[0]:
                count_by_files[split_result[2]] = count_by_files.pop(
                    split_result[1]) + 1 if split_result[1] in count_by_files else 1
    return count_by_files


def get_git_log_result(root_path: str, after: str = None, before: str = None, allowed_extensions: list = None):
    try:
        after_option = f"--after={after}" if after else ""
        before_option = f"--after={before}" if before else ""
        command = f'git log --name-status {after_option} {before_option} --pretty=format: | grep "."'
        process = subprocess.run([command], text=True, shell=True, check=False,
                                 cwd=root_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = process.stdout.splitlines()
        commit_counts_by_files = get_count_by_files(result)
        real_files = traversing_dir_for_file(root_path, allowed_extensions)

        for file_name in commit_counts_by_files.copy():
            if file_name not in real_files:
                del commit_counts_by_files[file_name]

        commit_counts_by_files = dict(
            sorted(commit_counts_by_files.items(), key=lambda item: item[1], reverse=True))
        return commit_counts_by_files
    except subprocess.CalledProcessError:
        return {}
