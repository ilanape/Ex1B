import sys


def compress():
    try:
        input_file = open("Input Text File", "r")
    except IOError:
        print('"Input Text File" does not exist')
    finally:
        input_file.close()

    # input file parsing

    compressed_version = open("Compressed version", "w")
    compressed_length = open("Compressed length", "w")
    compressed_version.close()
    compressed_length.close()


def decompress():
    print()


def compare():
    print()


if __name__ == "__main__":
    if sys.argv[1] == 'compress':
        compress()
    elif sys.argv[1] == 'decompress':
        decompress()
    elif sys.argv[1] == 'compare':
        compare()
    else:
        print('Invalid format: Huffman_Coding.py [compress/decompress/compare]')
