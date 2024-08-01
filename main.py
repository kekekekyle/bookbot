def main():
    book_path = "books/frankenstein.txt" 

    book_contents = read_book(book_path)
    word_count = count_words(book_contents)
    char_count = count_chars(book_contents)
    report(book_path, word_count, char_count)

def read_book(path):
    with open(path) as f:
       return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    result = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in result:
            result[lower_char] += 1
        else:
            result[lower_char] = 1
    return result

def sort_on(dict):
    return dict["count"]

def sort_chars(dict):
    result = []
    for char in dict:
        if char.isalpha():
            result.append({ "char": char, "count": dict[char] })
    return result

def report(path, word_count, char_count):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print(f"")

    char_count = sort_chars(char_count)
    char_count.sort(reverse=True, key=sort_on)
    for char in char_count:
        print(f"The '{char['char']}' character was found {char['count']} times")
    print(f"--- End report ---")

main()
