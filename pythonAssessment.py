import re


def count_specific_word(word, text):

    searched_word = word.lower()
    words = re.findall(r"\b\w+\b", text.lower())

    instance = 0
    for w in words:
        if w == searched_word:
            instance += 1

    print(instance)
    return instance


# def indentify_most_common_word(text):


with open("text.txt", "r", encoding="utf-8") as f:
    text = f.read()

count_specific_word("AI", text)
