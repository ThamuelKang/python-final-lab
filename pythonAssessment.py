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


def indentify_most_common_word(text):
    words = re.findall(r"\b\w+\b", text.lower())

    if not words:
        return None

    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    most_common_word = max(word_counts, key=word_counts.get)
    print(most_common_word)
    return most_common_word


def calculate_average_word_length(text):

    words = re.findall(r"\b\w+\b", text)

    if not words:
        return 0

    total_length = 0

    for word in words:
        word_length = len(word)
        total_length += word_length

    average_length = total_length / len(words)
    print(average_length)
    return average_length


with open("text.txt", "r", encoding="utf-8") as f:
    text = f.read()

count_specific_word("AI", text)
indentify_most_common_word(text)
calculate_average_word_length(text)
