import string

def get_book_text(textfile):
    with open(textfile) as f:
        fcont = f.read()
        return fcont

def count_words(text):
    num_words = 0
    twords = text.split()
    for i in twords:
        num_words = num_words + 1
    return num_words

def count_letters(text):
    dict_count = {}
    for i in text:
        i = i.lower()
        if i in dict_count:
            dict_count[i] += 1
        else:
            dict_count[i] = 1
    s_dict_count = dict(sorted(dict_count.items()))
    print(s_dict_count)
