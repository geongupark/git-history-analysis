"""For file system"""
import os


def is_allowed_file(file_name: str, allowed_extensions: list) -> bool:
    """
    Method For checking exetension
    Args:
        file_name (str): file name
        allowed_extensions (list): Allowed exetension list
    Returns:
        bool : Is allowed file
    """
    allowed_extensions = set(allowed_extensions)
    return "." in file_name and file_name.rsplit(".", 1)[1] in allowed_extensions


def traversing_dir_for_file(target_path: str = "./", allowed_extensions: list = None) -> list:
    """
    Get file list that are target exetension below the target path. (recursive)
    Args:
        target_path (str): target path, Default value is './'
        allowed_extensions (list): Allowed exetension list, Default value is None
    Returns:
        list : target list
    """
    matched_files = []
    for root, _dirs, files in os.walk(target_path):
        for file in files:
            file_full_path = os.path.join(root, file)
            if not allowed_extensions:
                matched_files.append(file_full_path)
            elif is_allowed_file(file_full_path, allowed_extensions):
                matched_files.append(file_full_path)
    return matched_files
