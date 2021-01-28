# WordCounter
Python 3 word counter


### Usage ###

To run the word_counter.py:

    Command : python <Path_to_project>/word_counter.py <Path_to_file>/{filename}.txt

1. First go into the project root directory

2. Run command below

example from project root directory:

    python ./word_counter.py ./testfiles/test1.txt


### Tests ###

To run the test:

1. First go into the project root directory

2. Run command below
   
example from project root directory:
   
    ./counttests.py

### Solution Explanation ###

COUNT - using a for loop to iterate through the file and split by space character, 
and add each word to a dictionary with word as key and count as value.

Time complexity:
loop through each word and adding / incrementing them in a dictionary O(n)

Considerations:
1. Must iterate through each word at least once to find if there are multiple occurrences thus using a for loop.
2. Incrementing the count for a specific word. Using dictionary with a search complexity of O(n)

SORT - using merge sort to sort through the unsorted list and compare by the occurrences.

Time complexity:
merge sort O(log n)

Considerations:
1. Considered using quicksort since it is sample data. Would be quick if dataset is not large.
2. Since the file can be of any size used merge sort in case of long files.








