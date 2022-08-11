import re
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""

    dictionary = dict()

    filepath = open(file, "r")

    words = re.sub(r'[^\w\s]', '', filepath.read()).lower().split()
    deleted_stop_words = [x for x in words if x not in STOP_WORDS]

    for words in deleted_stop_words:
        if words in dictionary:
            dictionary[words] = dictionary[words] + 1
        else:
            dictionary[words] = 1
    sorted_counts = sorted(
        dictionary.items(), key=lambda item: item[1], reverse=True)

    for allKeys in sorted_counts:
        print(allKeys[0], "| ", end="")
        print(end="")
        print(allKeys[1], end=" ")
        print((allKeys[1] * "*"), end=" ")
        print()


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
