# -------------------------------------------------Imports--------------------------------------------------------------

import os
from dataclasses import dataclass
import time
import re

# -------------------------------------------------Globals--------------------------------------------------------------

#dir_name = 'C:\\Users\\Mohamad-PC\\PycharmProjects\\google\\Archive\\'
dir_name = 'C:\\Users\\Mohamad-PC\\PycharmProjects\\google\\test\\'
dict = {}

# --------------------------------------------------Class---------------------------------------------------------------


@dataclass
class Node:
    def __init__(self, completed_sentence: str, source_text: str):
        self.completed_sentence = completed_sentence
        self.source_text = source_text

    def __str__(self):
        return "completed_sentence: " + self.completed_sentence + ', ' + "source_text: " + self.source_text

    def __lt__(self, other):
        return self.completed_sentence < other.completed_sentence
@dataclass
class AutoCompleteData(Node):
    def __init__(self, completed_sentence: str, source_text: str, offset: int, score: int):
        self.completed_sentence = completed_sentence
        self.source_text = source_text
        self.offset = offset
        self.score = score

    def __str__(self):
        return "completed_sentence: " + self.completed_sentence + ',' + "source_text: " + self.source_text

# --------------------------------------------------Function------------------------------------------------------------


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


if __name__ == "__main__":

    print("start")

    for file_name, stat in mapping_files_in_folders(dir_name):
        with open(file_name, encoding='utf-8') as file:
            for line in file:
                line = " ".join(re.sub(r"[^a-zA-Z0-9]", ' ', line).split())
                add_to_dict(line, file_name)
    for key in dict.keys():
        dict[key].sort()

    for key in dict:
        print("=" * 20)
        print("key: ", key)
    #     print("-" * 20)
        for a in dict[key]:
           print(a)

    print("end")