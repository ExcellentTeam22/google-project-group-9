# --------------------------------------------------Imports---------------------------------------------------------------
from dataclasses import dataclass
from typing import Tuple


# --------------------------------------------------Classes---------------------------------------------------------------
@dataclass
class Node:
    """
    Class to save all the data(sentences).
    """
    def __init__(self, completed_sentence: str, source_text: str):
        """
        Constructor.
        :param completed_sentence: Complete sentence after editing for quick search.
        :param source_text: The path of the original sentence(in the files).
        """
        self.completed_sentence = completed_sentence
        self.source_text = source_text

    def __str__(self):
        return "completed_sentence: " + self.completed_sentence + '\n' + "source_text: " + self.source_text + '\n'

    def __lt__(self, other):
        return self.completed_sentence < other.completed_sentence

    def __eq__(self, other):
        return self.completed_sentence == other.completed_sentence

    def __hash__(self):
        return hash((self.completed_sentence, self.source_text))

    def get_completed_sentence(self):
        return self.completed_sentence


# ----------------------------------------------------------------------------------------------------------------------
@dataclass
class AutoCompleteData:
    def __init__(self, completed_sentence: str, source_text: str, offset: int, score: int):
        self.completed_sentence = completed_sentence
        self.source_text = source_text
        self.offset = offset
        self.score = score

    def __str__(self):
        return "completed_sentence: " + self.completed_sentence + ',' + "source_text: " + self.source_text


# ----------------------------------------------------------------------------------------------------------------------
@dataclass
class TrieNode:
    """
    Our trie node implementation. Very basic. but does the job
    """

    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.word_finished = False
        self.counter = 1

    def add(self, word: str):
        """
        Adding a word in the trie structure
        """
        node = self
        for char in word:
            found_in_child = False
            for child in node.children:
                if child.char == char:
                    child.counter += 1
                    node = child
                    found_in_child = True
                    break
            if not found_in_child:
                new_node = TrieNode(char)
                node.children.append(new_node)
                node = new_node
        node.word_finished = True

    def find_prefix(self, prefix: str) -> Tuple[bool, int, bool]:
        """
        Check and return
          1. If the prefix exists in any of the words we added so far
          2. If yes then how may words actually have the prefix
        :param prefix:
        :return: This function returns tuple with three parameters:
                  1.Boolean: If the prefix exists as complete word.
                  2.Integer: Counter for the number of sentences that contains this prefix.
                  3.Boolean: If the given prefix exists in the tree.
        """
        node = self
        if not self.children:
            return False, 0, False
        for char in prefix:
            char_not_found = True
            for child in node.children:
                if child.char == char:
                    char_not_found = False
                    node = child
                    break
            if char_not_found:
                return False, 0, node.word_finished

        return True, node.counter, node.word_finished

    def get_leaves(self, prefix, array_of_leaves: []):
        """
        This recursive function gets the subtree, from "find_prefix_leaves".
        :param prefix: The given prefix.
        :param array_of_leaves: a reference for list.
        """
        for child in self.children:
            if child.word_finished:
                array_of_leaves.append(prefix + child.char)
            child.get_leaves(prefix + child.char, array_of_leaves)

    def find_prefix_leaves(self, prefix: str) -> []:
        """
        This function responsible for getting the leaves of the given prefix.
        :param prefix: String of prefix words.
        :return: Returns list of all the found leaves(complete words), for specific prefix.
        """
        node = self
        if not self.children:
            return []
        pref = ""
        for char in prefix:
            char_not_found = True
            for child in node.children:
                if child.char == char:
                    pref += char
                    char_not_found = False
                    node = child
                    break
            if char_not_found:
                return []
        array_to_return = []
        node.get_leaves(pref, array_to_return)
        return array_to_return

    def print_trie(self):
        """
        This function prints the tree, just for debugging.
        """
        print("the current root: ", self.char)
        print("the current root children: ")
        for child in self.children:
            print(child.char)
        print("-" * 20)
        for child in self.children:
            child.print_trie()
