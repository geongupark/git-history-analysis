"""Console script for git_log_analysis."""
import sys

from .git_log_analysis import get_git_log_result
from .utils.argument_parser import ArgumentParser


def main():
    """Console script for git_log_analysis."""
    args = ArgumentParser().get_args()

    root_path = args.root
    histogram = args.histogram
    output_path = args.output
    after = args.after
    before = args.before
    allowed_extensions = args.alloedext

    # Analyze git log
    commit_counts_by_files = get_git_log_result(
        root_path, after, before, allowed_extensions)

    # Plot histogram
    if histogram:
        pass

    # Save output file
    if output_path:
        pass

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
