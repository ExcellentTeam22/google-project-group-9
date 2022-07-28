# -------------------------------------------------Imports--------------------------------------------------------------
import os
import re
from classes import *


# --------------------------------------------------Function------------------------------------------------------------
def print_line_from_dict(key: str, dict: {}) -> None:
    """
    This function prints line from dict in a beautifully format.
    :param key: given word.
    :param dict: The given dictionary.
    """
    print("=" * 20)
    print("key: ", key)
    print("-" * 20)
    for node in dict[key]:
        print(node)


def mapping_files_in_folders(dir_name: str, traversed: list = [], results: list = []) -> list:
    """
    This function responsible for mapping the given files.
    :param dir_name: The path for the given directory.
    :param traversed: List of all the paths of the directories.
    :param results: reference for the results list.
    :return: List of the results.
    """
    dirs = os.listdir(dir_name)
    if dirs:
        for f in dirs:
            new_dir = dir_name + f + '/'
            if os.path.isdir(new_dir) and new_dir not in traversed:
                traversed.append(new_dir)
                mapping_files_in_folders(new_dir, traversed, results)
            else:
                results.append([new_dir[:-1], os.stat(new_dir[:-1])])
    return results


def add_new_word_to_data_base(line_in_file, path, dict: {}, trie):
    """
    This function adds the lines from the files to our dictionary.
    :param line_in_file: given line from the file.
    :param path: The location of the file that contains the specific line.
    :param dict: The given dictionary.
    :param trie: The given tree.
    """
    for word in line_in_file.split():
        node = Node(line_in_file, path)
        if word not in dict.keys():
            trie.add(word)
            dict[word] = [node]
        else:
            dict[word].append(node)


def get_dict_by_offline(dict, dir_name, trie):
    """
    This function is the main offline function.
    :param dict: The given dictionary.
    :param dir_name: path for our directory that we will map it.
    :param trie: The given tree.
    """
    for file_name, stat in mapping_files_in_folders(dir_name):
        with open(file_name, encoding='utf-8') as file:
            for line in file:
                line = " ".join(re.sub(r"[^a-zA-Z0-9]", ' ', line).split())
                add_new_word_to_data_base(line, file_name, dict, trie)
    for key in dict.keys():
        dict[key].sort()
