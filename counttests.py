import unittest

from util.counter import Counter
from util.sorter import TopWordSort


class TestWordCount(unittest.TestCase):

    def test_empty_file(self):
        counter = Counter('testfiles/emptyfile.txt')
        sorter = TopWordSort([(k, v) for k, v in counter.word_occurrence.items()])
        self.assertEqual(counter.total_words, 0)
        self.assertEqual(len(sorter.sorted_list), 0)

    def test_less_word_file(self):
        counter = Counter('testfiles/filewithlessthan10words.txt')
        sorter = TopWordSort([(k, v) for k, v in counter.word_occurrence.items()])
        self.assertEqual(counter.total_words, 3)
        self.assertEqual(len(sorter.sorted_list), 3)

    def test_non_letters_file(self):
        counter = Counter('testfiles/filewithnonletters.txt')
        sorter = TopWordSort([(k, v) for k, v in counter.word_occurrence.items()])
        self.assertEqual(counter.total_words, 47)
        self.assertEqual(len(sorter.sorted_list), 10)
        self.assertEqual(sorter.sorted_list[0][0], 'ten')

    def test_random_word_file(self):
        counter = Counter('testfiles/randomwordfile.txt')
        sorter = TopWordSort([(k, v) for k, v in counter.word_occurrence.items()])
        self.assertEqual(counter.total_words, 200)
        self.assertEqual(len(sorter.sorted_list), 103)
        self.assertEqual(sorter.sorted_list[0][0], 'nunc')

