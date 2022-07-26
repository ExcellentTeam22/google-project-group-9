# -------------------------------------------------Imports--------------------------------------------------------------

import os
from dataclasses import dataclass
import time
import re
from functools import reduce

from classes import *

# -------------------------------------------------Globals--------------------------------------------------------------

# dir_name = 'C:\\Users\\Mohamad-PC\\Desktop\\google\\google-project-group-9\\Archive\\'
dir_name = 'C:\\Users\\Mohamad-PC\\Desktop\\google\\google-project-group-9\\test\\'
dict = {}


# --------------------------------------------------Function------------------------------------------------------------

def print_line_from_dict(key: str) -> None:
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


def add_to_dict(line_in_file, path):
    for word in line_in_file.split():
        node = Node(line_in_file, path)
        if word not in dict.keys():
            dict[word] = [node]
        else:
            dict[word].append(node)


def get_minimum_list(list_of_lists: []) -> []:
    return min(list_of_lists, key=lambda list: len(list))


def intersect_lists(list_of_lists : []):
    minimum_list = get_minimum_list(list_of_lists)
    """for list in list_of_lists:
        result = set(minimum_list).intersection(list)"""
    #return (set(minimum_list).intersection(list) for list in list_of_lists)
    return list(reduce(set.intersection, [set(item) for item in list_of_lists]))



if __name__ == "__main__":

    """print("start")

    for file_name, stat in mapping_files_in_folders(dir_name):
        with open(file_name, encoding='utf-8') as file:
            for line in file:
                line = " ".join(re.sub(r"[^a-zA-Z0-9]", ' ', line).split())
                add_to_dict(line, file_name)
    for key in dict.keys():
        dict[key].sort()

    print("end")"""
    print(intersect_lists([["as4x","44", 99, "a"],["asx","asx","44","asx", 99],["asx", 99, "44"]]))
