# -------------------------------------------------Imports--------------------------------------------------------------

import os
from dataclasses import dataclass
import time
import re
from functools import reduce

from classes import *


# -------------------------------------------------Globals--------------------------------------------------------------


# --------------------------------------------------Function------------------------------------------------------------

def print_line_from_dict(key: str, dict: {}) -> None:
    print("=" * 20)
    print("key: ", key)
    print("-" * 20)
    for node in dict[key]:
        print(node)


def mapping_files_in_folders(dir_name: str, traversed: list = [], results: list = []) -> list:
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


def add_to_dict(line_in_file, path, dict: {}):
    for word in line_in_file.split():
        node = Node(line_in_file, path)
        if word not in dict.keys():
            dict[word] = [node]
        else:
            dict[word].append(node)



def get_dict_by_offline(dict, dir_name):
    for file_name, stat in mapping_files_in_folders(dir_name):
        with open(file_name, encoding='utf-8') as file:
            for line in file:
                line = " ".join(re.sub(r"[^a-zA-Z0-9]", ' ', line).split())
                add_to_dict(line, file_name, dict)
    for key in dict.keys():
        dict[key].sort()
