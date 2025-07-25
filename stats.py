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
    new_list = []
    for i in text:
        i = i.lower()
        if (i in string.ascii_lowercase) or (i in "æâêëô"):
            if i in dict_count:
                dict_count[i] += 1
            else:
                dict_count[i] = 1
    for k, v in dict_count.items():
        new_list.append({"char": k, "num": v})
    return new_list
    #return dict_count
    #s_dict_count = dict(sorted(dict_count.items()))
    #print(s_dict_count)

def sort_dict(things):
    things.sort()
    for i in things:
        print(i)
