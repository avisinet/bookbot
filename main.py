from stats import get_book_text, count_words, count_letters, sort_dict
def main():
    txt = get_book_text("./books/frankenstein.txt")

    twords = count_words(txt)

    print(f"{twords} words found in the document")

    char_list = count_letters(txt)
    #print(char_list)

    sort_dict(char_list)


main()
