from OfflinePart import *
from OnlinePart import *


# dir_name = 'C:\\Users\\Mohamad-PC\\Desktop\\google\\google-project-group-9\\google-project-group-9\\Archive\\'
dir_name = 'C:\\Users\\Mohamad-PC\\Desktop\\google\\google-project-group-9\\google-project-group-9\\test\\'

dict = {}
trie = TrieNode("*")


if __name__ == "__main__":

    print("start")

    print("start offline")
    print("=" * 20)
    get_dict_by_offline(dict, dir_name, trie)
    print("End offline")
    print("=" * 20)

    print("start online")
    print("=" * 20)
    online_function(dict, trie)
    print("end online")
    print("=" * 20)

    print("end")

