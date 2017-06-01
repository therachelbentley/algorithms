from trie.build_trie import  build_trie


def trie_matching(text, trie):
    # keep track of the pattern it"s matching on
    pattern = ""

    # start at root node
    v = trie[0] # root

    # step through text to find matching
    for char in text:
        # reached the end of that pattern
        if v is None:
            return pattern
        # check if char is in the current trie node
        elif char in v:
            pattern += char
            v = trie.get(v[char], None)
            if v is None:
                return pattern
        # char does not match any nodes
        else:
            return None


def match(text, patterns):
    """ Searches for patterns inside of a text.

    Args:
        text (str): The text to search.
        patterns (list): A list of patterns to search
            for in the text.

    Returns:
        A list of tuples. The first item in a tuple
        represents the index a pattern began matching
        on. The second item represents the pattern that
        matched.
    """
    result = []

    if not text or not patterns:
        return result

    # build trie from patterns
    trie = build_trie(patterns)    

    # each char in text could be the start of a pattern
    i = 0
    while text:
        match = trie_matching(text, trie)
        if match is not None:
            result.append((i, match))
        text = text[1:]
        i += 1

    return result


### TESTS ###
case_one_text = "AAA"
case_one_patterns = ["AA"]
assert match(case_one_text, case_one_patterns) == [(0, "AA"), (1, "AA")]

case_two_text = "AA"
case_two_patterns = ["T"]
assert match(case_two_text, case_two_patterns) == []


case_three_text = "AATCGGGTTCAATCGGGGT"
case_three_patterns = ["ATCG", "GGGT"]
assert match(case_three_text, case_three_patterns) == [(1, "ATCG"), (4, "GGGT"), (11, "ATCG"), (15, "GGGT")]
