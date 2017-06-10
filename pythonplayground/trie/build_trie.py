

def build_trie(strings):
    """ Builds a trie out of a given list of strings.

        Input:
            strings (list): A list of strings.
        Output:
            A dictionary where the keys are the node ids and the values
            are a dictionary of the node"s children.
    """

    # initialize trie
    trie = {}

    # keep track of what the next node id should be
    new_node = 1

    for string in strings:
        current_node = 0
        last_char = len(string) - 1

        for i, character in enumerate(string):

            # if the current node does not exist in the dict then add it
            if not current_node in trie:
                trie[current_node] = {}

            # if character is already a child of current_node
            # then current_node now becomes that child's id
            # else create a new node for that character
            if character in trie[current_node]:
                current_node = trie[current_node][character]
            else:
                trie[current_node][character] = new_node
                current_node = new_node
                new_node += 1

            # if this is the last character in the pattern
            # then make one of it children indicate its
            # a leaf node
            if i == last_char:
                if not current_node in trie:
                    trie[current_node] = {}
                trie[current_node]["LEAF"] = string

    return trie


### TESTS ###
case_one = ["ATA"]
assert build_trie(case_one) == {0: {"A": 1}, 1: {"T": 2}, 2: {"A": 3}, 3: {"LEAF": "ATA"}}

case_two = ["AT", "AG", "AC"]
assert build_trie(case_two) == {0: {"A": 1}, 1: {"G": 3, "T": 2, "C": 4}, 2: {"LEAF": "AT"}, 3: {"LEAF": "AG"}, 4: {"LEAF": "AC"}}

case_three = ["ATAGA", "ATC", "GAT"]
assert build_trie(case_three) == {0: {"G": 7, "A": 1}, 1: {"T": 2}, 2: {"C": 6, "A": 3}, 3: {"G": 4}, 4: {"A": 5}, 5: {"LEAF": "ATAGA"}, 6: {"LEAF": "ATC"}, 7: {"A": 8}, 8: {"T": 9}, 9: {"LEAF": "GAT"}}

case_four = ["AT", "A", "AG"]
assert build_trie(case_four) == {0: {"A": 1}, 1: {"G": 3, "T": 2, "LEAF": "A"}, 2: {"LEAF": "AT"}, 3: {"LEAF": "AG"}}
