def count_words(text):
    words_list = text.split()
    num_words = len(words_list)
    return num_words


def count_char(text):
    count_dict = {}
    lower_words = text.lower()
    unique_char = set(lower_words)
    for u in unique_char:
        count_dict[u] = lower_words.count(u)
    return count_dict

def sort_on(items):
    return items["num"]

def sort_dict(char_dict):
    char_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    char_list.sort(reverse=True, key=sort_on)
    return char_list
