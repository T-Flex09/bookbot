import sys
from stats import *

def sort_on(items):
    return items["num"]

def get_book(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print('Usage:\n python3 main.py <path_to_book>')
        sys.exit(1)
    file = sys.argv[1]
    char_table = get_char_density(get_book(file))
    char_array = []
    for k, v in char_table.items():
        char_array.append({"name": k, "num": v})
    char_array.sort(reverse=True, key=sort_on)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {file}\n----------- Word Count ----------\nFound {get_word_count(get_book(file))} total words\n--------- Character Count -------")
    for dicsh in char_array:
        print(f"{dicsh['name']}: {dicsh['num']}")
    print('============= END ===============')

main()
