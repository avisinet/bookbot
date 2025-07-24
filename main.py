from stats import get_book_text, count_words, count_letters

def main():
    txt = get_book_text("./books/frankenstein.txt")

    twords = count_words(txt)

    print(f"{twords} words found in the document")

    characters = count_letters(txt)


main()
