"""Console script for git_log_analysis."""
import sys

from git_log_analysis.plot_histogram import plot_histogram
from git_log_analysis.utils.file_system import save_dict_to_json
from git_log_analysis.git_log_analyzer import get_git_log_result
from git_log_analysis.utils.argument_parser import ArgumentParser


def main():
    """Console script for git_log_analysis."""
    args = ArgumentParser().get_args()

    root_path = args.root
    histogram = args.histogram
    output_path = args.output
    after = args.after
    before = args.before
    allowed_extensions = args.allowedext

    # Analyze git log
    commit_counts_by_files = get_git_log_result(
        root_path, after, before, allowed_extensions)

    # Plot histogram
    if histogram:
        plot_histogram(commit_counts_by_files)

    # Save output file
    if output_path:
        save_dict_to_json(output_path, commit_counts_by_files)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
