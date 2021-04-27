import filecmp
from collections import Counter
from queue import PriorityQueue
from TreeNode import TreeNode


def compress():
    # input file parsing
    try:
        input_file = open("Input Text File", "r")
    except IOError:
        print('"Input Text File" does not exist')
        input_file.close()

    text_file = input_file.read()
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
    table_to_share = huffman_code(queue.get())

    # output files creation
    length = 0
    compressed_version = open("Compressed version", "w")
    compressed_length = open("Compressed length", "w")

    for letter in text_file:
        compressed_version.write(table[letter])
        length += len(table_to_share[letter])

    compressed_length.write(str(length))
    compressed_version.close()
    compressed_length.close()

    return table_to_share


def huffman_code(node, binary_string=""):
    d = dict()
    # leaf node
    if node.has_children() is False:
        return {node.get_letter(): binary_string}

    # internal node - build recursively
    left, right = node.get_children()
    d.update(huffman_code(left, binary_string + '0'))
    d.update(huffman_code(right, binary_string + '1'))
    return d


def decompress(self, file, shared_table):
    # input file parsing
    try:
        input_file = open(file, "r")
    except IOError:
        print('file does not exist')
        input_file.close()

    encoded_text = input_file.read()
    # output file creation
    decoded_text = open("Decoded Text", "w")
    code = ""
    for bit in encoded_text:
        code += bit
        # code is in table
        if code in shared_table.values():
            decoded_text.write(self.get_key(code))
            code = ""

    decoded_text.close()


def get_key(code):
    for key, val in table.items():
        if code == val:
            return key


if __name__ == "__main__":
    table = compress()
    decompress("Compressed version", table)
    if filecmp.cmp("Input Text File", "Decoded Text", shallow=False):
        print("good")
    else:
        print("bad")
