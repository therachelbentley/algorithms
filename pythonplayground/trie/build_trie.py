

def build_trie(strings):
    """ Builds a trie out of a given list of strings.

        Input:
            strings (list): A list of strings.
        Output:
            A dictionary where the keys are the node ids and the values
            are a dictionary of that nodes children.
    """

    # initialize trie
    trie = {}

    # keep track of what the next node id should be
    new_node = 1

    for string in strings:
        current_node = 0
        for character in string:

            # if the current node does not exist in the dict then add it
            if not current_node in trie:
                trie[current_node] = {}

            # if the character is already a child of the current node
            # then set the current node to be the character node"s id
            # else create a new node for that character
            if character in trie[current_node]:
                current_node = trie[current_node][character]
            else:
                trie[current_node][character] = new_node
                current_node = new_node
                new_node += 1

    return trie


### TESTS ###
case_one = ["ATA"]
assert build_trie(case_one) == {0: {"A": 1}, 1: {"T": 2}, 2: {"A": 3}}

case_two = ["AT", "AG", "AC"]
assert build_trie(case_two) == {0: {"A": 1}, 1: {"G": 3, "T": 2, "C": 4}}

case_three = ["ATAGA", "ATC", "GAT"]
assert build_trie(case_three) == {0: {"A": 1, "G": 7}, 1: {"T": 2}, 2: {"A": 3, "C": 6}, 3: {"G": 4}, 4: {"A": 5}, 7: {"A": 8}, 8: {"T": 9}}
