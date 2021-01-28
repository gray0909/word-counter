import argparse
from util.counter import Counter
from util.sorter import TopWordSort

if __name__ == '__main__':

    file_path = ""
    top_word_count = 10

    parser = argparse.ArgumentParser(description='Count words in a file, prints top 10 occurrences')
    parser.add_argument("file_path", type=str, help="File path of file to be read")

    args = parser.parse_args()

    if 'file_path' in args:
        file_path = args.file_path
        print('File path: {}'.format(file_path))

    counter_obj = Counter(file_path)
    sorted_obj = TopWordSort([(k, v) for k, v in counter_obj.word_occurrence.items()])

    print("Total number of words: {}".format(counter_obj.total_words))
    for w, c in enumerate(sorted_obj.sorted_list[0:10]):
        print('Top {}: word = {}, occurrences = {}'.format(w+1, c[0], c[1]))




