def get_num_words(text):
    return len(text.split())


def count_characters(text):
    count = {}
    for char in text.lower():
        count[char] = count.get(char, 0) + 1
    return count 



def sort_character_dict(dict):
    l = []
    for key in dict:
        if key.isalpha():
            l.append({"char": key, "num": dict[key]})
    l.sort(key=sort_on, reverse=True)
    return l


def sort_on(e):
    return e["num"]



