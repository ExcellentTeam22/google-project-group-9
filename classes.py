# --------------------------------------------------Class---------------------------------------------------------------
from dataclasses import dataclass


@dataclass
class Node:
    def __init__(self, completed_sentence: str, source_text: str):
        self.completed_sentence = completed_sentence
        self.source_text = source_text

    def __str__(self):
        return "completed_sentence: " + self.completed_sentence + '\n' + "source_text: " + self.source_text + '\n'

    def __lt__(self, other):
        return self.completed_sentence < other.completed_sentence

    def __eq__(self, other):
        return self.completed_sentence == other.completed_sentence

    def __hash__(self):
        return hash((self.completed_sentence,self.source_text))

    def get_completed_sentence(self):
        return self.completed_sentence



@dataclass
class AutoCompleteData:
    def __init__(self, completed_sentence: str, source_text: str, offset: int, score: int):
        self.completed_sentence = completed_sentence
        self.source_text = source_text
        self.offset = offset
        self.score = score

    def __str__(self):
        return "completed_sentence: " + self.completed_sentence + ',' + "source_text: " + self.source_text