from trie.build_trie import  build_trie


def trie_matching(text, trie):
    # keep track of the pattern it's matching on
    patterns = []

    # start at root node
    v = trie[0]
    last_char = len(text) - 1

    # step through text to find matches
    for i, char in enumerate(text):
        # reached the end of a pattern
        if v.get("LEAF"):
            patterns.append(v["LEAF"])

        # check if char is in the current trie node
        if char in v:
            v = trie[v[char]]
            if i == last_char and v.get("LEAF"):
                patterns.append(v["LEAF"])
        # char does not match any nodes
        else:
            return patterns

    return patterns


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
        if match:
            result.append((i, match))
        text = text[1:]
        i += 1

    return result


### TESTS ###
case_one_text = "AAA"
case_one_patterns = ["AA"]
assert match(case_one_text, case_one_patterns) == [(0, ["AA"]), (1, ["AA"])]

case_two_text = "AA"
case_two_patterns = ["T"]
assert match(case_two_text, case_two_patterns) == []


case_three_text = "AATCGGGTTCAATCGGGGT"
case_three_patterns = ["ATCG", "GGGT"]
assert match(case_three_text, case_three_patterns) == [(1, ["ATCG"]), (4, ["GGGT"]), (11, ["ATCG"]), (15, ["GGGT"])]

case_four_text = "AATCG"
case_four_patterns = ["ATCG", "GGGT", "AT"]
assert match(case_four_text, case_four_patterns) == [(1, ['AT', 'ATCG'])]
