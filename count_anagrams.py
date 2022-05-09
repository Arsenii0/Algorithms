# Example 1:

# Input:
#     txt = forxxorfxdofr
#     pat = for
#     Output: 3
#     Explanation: for, orf and ofr appears
#     in the txt, hence answer is 3.


from collections import defaultdict


def search_anagrams(txt, pat):
    anagrams_count = 0
    pattern_symbols = defaultdict(int)
    for symbol in pat:
        pattern_symbols[symbol] += 1

    current_symbols_count_map = defaultdict(int)

    for current_index in range(0, len(pat)):
        current_symbols_count_map[txt[current_index]] += 1
        current_index += 1

    anagrams_count = 1 if current_symbols_count_map == pattern_symbols else 0

    while current_index < len(txt):
        # window sliding technique: add the next symbol and remove one at the beginning
        current_symbol = txt[current_index]
        start_symbol = txt[current_index - len(pat)]

        current_symbols_count_map[current_symbol] += 1
        current_symbols_count_map[start_symbol] -= 1

        if current_symbols_count_map[start_symbol] == 0:
            current_symbols_count_map.pop(start_symbol)

        if current_symbols_count_map == pattern_symbols:
            anagrams_count += 1

        current_index += 1

    return anagrams_count


def main():
    txt = "forxxorfxdofr"
    pat = "for"
    print(search_anagrams(txt, pat))


if __name__ == "__main__":
    main()
