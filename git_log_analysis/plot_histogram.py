"""Plotting histogram"""


def plot_histogram(gla_results: dict) -> None:
    """Plotting histogram

    Args:
        gla_results (dict): gla results
    """
    if not gla_results:
        print("No data! :)")
        return
    hist_width = 100
    longgest_file_path = max(list(gla_results.keys()), key=len)
    longgest_count = str(list(gla_results.values())[0])

    for file_path, count in gla_results.items():
        print('{:{width_path}s}  {:{width_count}s} | {:{width_hist}s} '.format(
            file_path,
            str(count),
            '■' * (hist_width if count > hist_width else count),
            width_path=len(longgest_file_path),
            width_count=len(longgest_count),
            width_hist=hist_width))


if __name__ == "__main__":
    results = {"abcd": 2204, "besfefdfef": 152,
               "csdf": 10, "ds": 2, "eeeee": 1}
    plot_histogram(results)
