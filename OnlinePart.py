from functools import reduce
from typing import List
from classes import *
# -----------------------------------------------------------------------------------------------------------------------

def get_minimum_list(list_of_lists: []) -> []:
    print(list_of_lists)
    return min(list_of_lists, key=lambda list: len(list))


def intersect_lists(list_of_lists: []):
    # minimum_list = get_minimum_list(list_of_lists)
    # # print("minimum_list: ",minimum_list)
    # for list in list_of_lists:
    #     minimum_list = set(minimum_list).intersection(list)
    #
    # return minimum_list

    return [] if not list_of_lists else list(reduce(set.intersection, [set(item) for item in list_of_lists]))

def grader(pref: str, array_of_sentences: []) -> []:
    return []

# -----------------------------------------------------------------------------------------------------------------------
def get_best_k_completions(prefix: str, dict: {}) -> List[AutoCompleteData]:

    # Check which word is the longest
    # longest_word = max(prefix.split(), key=len)
    words_in_list = prefix.split()
    # Search the longest_word from the prefix in the tree.
    """if trie.search(longest_word):
        # if longest_word in dict: ?????
        sentences = dict[longest_word]"""


# ----------------------------------------------------------------------------------------------------------------------

def get_list_of_lists(dict: {}, sentence: []) -> ([], []):
    ret = []
    not_completed_words = []
    for word in sentence:
        if word in dict.keys():
            ret.append(dict[word])
        else:
            not_completed_words.append(word)
    print(ret)
    print(not_completed_words)
    return ret, not_completed_words
    # return [(dict[word] for word in sentence if word in dict.keys() else []]


def reduces_according_by_order_sentence(string : str, sentences: []) -> []:
    return list(filter(lambda sentence: string in sentence.get_completed_sentence(), sentences))


def online_function(dict: {}):
    input_prefix = ""
    while input_prefix != "exit":
        input_prefix = input_prefix + input(f"Enter your text:\n{input_prefix}")
        if input_prefix == "":  # No input received
            pass
        elif input_prefix[-1] == "#":
            input_prefix = ""
        else:  # Input received - search 5 suggestions
            print("-" * 20)
            print(input_prefix)
            list_of_all_sentences_by_input, not_completed_words = get_list_of_lists(dict, input_prefix.split())
            # if len(not_completed_words) != 0:
            #     input_prefix = ""
            #     for word in list_of_all_sentences_by_input[0]:
            #         input_prefix += word.get_complete_
            list_of_intersected_sentences = intersect_lists(list_of_all_sentences_by_input)
            list_of_sentences_contain_prefix = reduces_according_by_order_sentence(input_prefix, list_of_intersected_sentences)
            # if len(list_of_sentences_contain_prefix) >= 5:
            list_of_sentences_contain_prefix.sort()
            print("list_of_intersected_sentences: ")
            for a in list_of_sentences_contain_prefix:
                print(list_of_sentences_contain_prefix.index(a)+1, a)
            else:
                get_best_k_completions(input_prefix, dict)
