from stats import get_book_text, count_words, count_letters, sort_dict
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    txt = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...")

    twords = count_words(txt)

    print(f"----------- Word Count ----------\nFound {twords} total words")

    char_list = count_letters(txt)
    #print(char_list)

    char_list.sort(reverse=True, key=sort_dict)
    print("--------- Character Count -------")
    for i in char_list:
        print(f"{i['char']}: {i['num']}") 
    print("============= END ===============")

main()
