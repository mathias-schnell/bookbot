def get_num_words(filepath):
    with open(filepath) as f:
        contents = f.read()
        words = len(contents.split())
    return words

def get_num_chars(filepath):
    char_dict = {}
    with open(filepath) as f:
        contents = f.read()
        words = contents.split()
        for word in words:
            word = word.lower()
            chars = list(word)
            for char in chars:
                if char in char_dict:
                    char_dict[char] += 1
                else:
                    char_dict[char] = 1
    return char_dict

def dict_sort(dict):
    return dict["num"]

def report_num_chars(char_dict):
    sorted_dict = []
    for char in char_dict:
        sorted_dict.append({"char": char, "num": char_dict[char]})
    sorted_dict.sort(reverse = True, key = dict_sort)
    return sorted_dict