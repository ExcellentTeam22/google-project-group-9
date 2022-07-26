from dataclasses import dataclass

# -----------------------------------------------------------------------------------------------------------------------
from typing import List


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
        super().__init__(completed_sentence, source_text)
        self.offset = offset
        self.score = score

    def __str__(self):
        return "completed_sentence: " + self.completed_sentence + ',' + "source_text: " + self.source_text


# -----------------------------------------------------------------------------------------------------------------------
def get_best_k_completions(prefix: str) -> List[AutoCompleteData]:
    # Check which word is the longest
    longest_word = max(prefix.split(), key=len)
    # Search the longest_word from the prefix in the tree.
    if trie.search(longest_word):
        # if longest_word in dict: ?????
        sentences = dict[longest_word]


# -----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    while True:
        input_prefix = input("Enter your text:\n")
        if input_prefix == "":  # No input received
            pass
        else:  # Input received - search 5 suggestions
            get_best_k_completions(input_prefix)
