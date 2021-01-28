import re


def format_word(word):
    return re.sub('[^a-z]+', '', str(word).lower())


class Counter:

    def __init__(self, file_path):
        self.file_path = file_path
        self.total_words = 0
        self.word_occurrence = dict()
        self.count_words()

    def count_words(self):
        with open(self.file_path, 'r', encoding="utf8") as file:
            for word in file.read().split():
                word = format_word(word)
                if word.strip() != '':
                    if word in self.word_occurrence:
                        self.word_occurrence[word] += 1
                    else:
                        self.word_occurrence.setdefault(word, 1)
                    self.total_words += 1
