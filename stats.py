def get_word_count(book):
    return len(book.split())

def get_char_density(book):
    char_table = {}
    words = book.strip().split()
    for word in words:
        for char in word:
            char = char.lower()
            if char in char_table:
                char_table[char] += 1
            else:
                char_table[char] = 1
    return char_table
