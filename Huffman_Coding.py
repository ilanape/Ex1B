import sys
from collections import Counter
from queue import PriorityQueue

from TreeNode import TreeNode


def compress():
    # input file parsing
    try:
        input_file = open("Input Text File", "r")
        text_file = input_file.read()
    except IOError:
        print('"Input Text File" does not exist')
        input_file.close()

    # compute frequencies
    freq = Counter(text_file)

    # create tree nodes
    # nodes are sorted by freq. increasing order using priority queue
    queue = PriorityQueue()
    for letter, f in freq.items():
        queue.put(TreeNode(letter, f))

    # create Huffman tree using the priority queue
    while queue.qsize() > 1:
        # two smallest freq. nodes
        left = queue.get()
        right = queue.get()
        # new internal node
        queue.put(TreeNode(None, left.freq + right.freq, left, right))

    # create Huffman code table
    table = huffman_code(queue.get())

    # output files creation
    length = 0
    compressed_version = open("Compressed version", "w")
    compressed_length = open("Compressed length", "w")

    for letter in text_file:
        compressed_version.write(table[letter])
        length = length + len(table[letter])

    compressed_length.write(str(length))
    compressed_version.close()
    compressed_length.close()


def huffman_code(node, binary_string=""):
    table = dict()
    # leaf node
    if node.has_children() is False:
        return {node.get_letter(): binary_string}

    # internal node - build recursively
    left, right = node.get_children()
    table.update(huffman_code(left, binary_string + '0'))
    table.update(huffman_code(right, binary_string + '1'))
    return table


def decompress():
    print()


def compare():
    print()


if __name__ == "__main__":
    # if sys.argv[1] == 'compress':
    #     compress()
    # elif sys.argv[1] == 'decompress':
    #     decompress()
    # elif sys.argv[1] == 'compare':
    #     compare()
    # else:
    #     print('Invalid format: Huffman_Coding.py [compress/decompress/compare]')

    compress()
