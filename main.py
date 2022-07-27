from OfflinePart import *
from OnlinePart import *


# dir_name = 'C:\\Users\\Mohamad-PC\\Desktop\\google\\google-project-group-9\\google-project-group-9\\Archive\\'
dir_name = 'C:\\Users\\Mohamad-PC\\Desktop\\google\\google-project-group-9\\google-project-group-9\\minitest2\\'
dict = {}
trie = TrieNode("*")


if __name__ == "__main__":

    print("start")

    print("start offline")
    print("=" * 20)
    get_dict_by_offline(dict, dir_name, trie)
    trie.print_trie()
    print("End offline")
    print("=" * 20)

    """print("start online")
    print("=" * 20)
    online_function(dict)
    print("end online")
    print("=" * 20)"""

    print("end")
    """root = TrieNode('*')
    root.add("hackathon")
    root.add('hack')
    root.add('abc')
    root.add('abd')


    #print(root.find_prefix('hac'))
    print(root.find_prefix_leaves('hac'))
    print(root.find_prefix('abc'))
    #print(root.find_prefix('hack'))
    #print(root.find_prefix('hackathon'))
    #print(root.find_prefix('ha'))
    print(root.find_prefix_leaves('ha'))
    print(root.find_prefix('hammer'))
    print(root.find_prefix_leaves('hammer'))"""

