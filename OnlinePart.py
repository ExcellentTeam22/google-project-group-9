from functools import reduce
from typing import List
from classes import *


# -----------------------------------------------------------------------------------------------------------------------
def get_minimum_list(list_of_lists: []) -> []:
    """
    This function returns the shortest list from given list of lists.
    :param list_of_lists: the given list of lists.
    :return: The shortest list.
    # """
    return min(list_of_lists, key=lambda list: len(list))


def intersect_lists(list_of_lists: []):
    """
    This function returns the intersected list, of list of lists.
    :param list_of_lists: The given list of lists.
    :return: The intersected list.
    """
    return [] if not list_of_lists else list(reduce(set.intersection, [set(item) for item in list_of_lists]))


def grader(pref: str, array_of_sentences: []) -> []:
    """
    The grader function.
    :param pref: The given prefix.
    :param array_of_sentences: The intersected list to check with the prefix.
    :return: List of all sentences with the grade according to the prefix.
    """
    return []


def get_best_k_completions(prefix: str, dict: {}) -> List[AutoCompleteData]:
    """
    This function returns the best k completions according to the grade.
    :param prefix: The given prefix.
    :param dict: dictionary of all the sentences.
    :return: list of the best fife results.
    """
    words_in_list = prefix.split()
    # Search the longest_word from the prefix in the tree.
    """if trie.search(longest_word):
        # if longest_word in dict: ?????
        sentences = dict[longest_word]"""


# ----------------------------------------------------------------------------------------------------------------------

def get_list_of_lists(dict: {}, sentence: []) -> ([], []):
    """
    This function gets the sentence and process it, then gets all the sentences that have the word.
    :param dict: dictionary of all the sentences.
    :param sentence: the given sentence.
    :return: Tuple of two lists.
    """
    ret = []
    not_completed_words = []
    for word in sentence:
        if word in dict.keys():
            ret.append(dict[word])
        else:
            not_completed_words.append(word)
    return ret, not_completed_words


def reduces_according_by_order_sentence(string : str, sentences: []) -> []:
    """
    This function filters given list according to given string.
    :param string: The given string
    :param sentences: List of sentences to filter them.
    :return:The filtered list.
    """
    return list(filter(lambda sentence: string in sentence.get_completed_sentence(), sentences))


def get_completion(pref: str, trie) -> []:
    """
    This function returns the possible completions.
    :param pref: The given prefix.
    :param trie: The given tree.
    :return: List of possible completions.
    """
    tuple_to_process = trie.find_prefix(pref)
    if tuple_to_process[0]:
        return trie.find_prefix_leaves(pref)
    return []


def online_function(dict: {}, trie):
    """
    This function is the main online function.
    :param dict: dictionary of all the sentences.
    :param trie: The given tree.
    """
    input_prefix = ""
    while input_prefix != "exit":
        list_of_all_sentences_by_input, not_completed_words = [], []
        input_prefix = input_prefix + input(f"Enter your text:\n{input_prefix}")
        if input_prefix == "":  # No input received
            pass
        elif input_prefix[-1] == "#":
            input_prefix = ""
        else:  # Input received - search 5 suggestions
            print("-" * 20)
            print(input_prefix)
            list_of_all_sentences_by_input, not_completed_words = get_list_of_lists(dict, input_prefix.split())

            if len(not_completed_words) == 0:

                list_of_intersected_sentences = intersect_lists(list_of_all_sentences_by_input)
                list_of_sentences_contain_prefix = reduces_according_by_order_sentence(input_prefix, list_of_intersected_sentences)
                # if len(list_of_sentences_contain_prefix) >= 5:
                list_of_sentences_contain_prefix.sort()
                print("list_of_intersected_sentences: ")
                for a in list_of_sentences_contain_prefix:
                    print(list_of_sentences_contain_prefix.index(a) + 1, a)
                else:
                    get_best_k_completions(input_prefix, dict)

            elif len(not_completed_words) == 1:
                list_of_completions = get_completion(input_prefix, trie)
                list_of_completions = list(sorted(list_of_completions, key=len))

                for new_completions in list_of_completions:
                    if len(list_of_sentences_contain_prefix) > 5:
                        list_of_sentences_contain_prefix.sort()
                        break
                    new_list_of_all_sentences_by_input = [new_completions] + list_of_all_sentences_by_input
                    list_of_intersected_sentences = intersect_lists(new_list_of_all_sentences_by_input)
                    new_input_prefix = input_prefix.replace(not_completed_words[0], input_prefix)
                    list_of_sentences_contain_prefix += reduces_according_by_order_sentence(new_input_prefix,
                                                                                       list_of_intersected_sentences)



                print("list_of_intersected_sentences: ")
                for a in list_of_sentences_contain_prefix:
                    print(list_of_sentences_contain_prefix.index(a) + 1, a)
                else:
                    get_best_k_completions(input_prefix, dict)
            else:
                print("You have too many wrong words, please check the input an try again!!!", not_completed_words)

