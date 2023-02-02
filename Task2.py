def unique_words(src_file):
    with open(src_file, "r") as src:
        lines = src.read().splitlines()
        unique = set(lines)
        return unique

def count_the_article(src_file):
    with open(src_file, "r") as src:
        lines = src.read().splitlines()
        unique = set(lines)
        return(len(unique))

def sorted_words(src_file):
    with open(src_file, "r") as src:
        lines = src.read().splitlines()
        unique = set(lines)
        return(sorted(unique, key=len, reverse=True))

def character_word_count(src_file):
    with open(src_file, "r") as src:
        lines = src.read().splitlines()
        unique = set(lines)
        count_dict = {}
        for i in unique:
            count_dict[i] = unique.count(i)
        return count_dict

def starts_with_vow(src_file):
    with open(src_file, "r") as src:
        lines = src.read().splitlines()
        # unique = set(lines)
        count = 0
        for i in lines:
            if i.startswith(("a","e","i","o","u")):
                count+=1
        
        return count

def rare_words(src_file):
    with open(src_file, "r") as src:
        lines = set(src.read().splitlines())
    with open("20k.txt", "r") as k:
        k_lines = set(k.read().splitlines())

    rare = lines - k_lines
    return rare

def unused_word(src_file1, src_file2, src_file3):
    with open(src_file1, "r") as f1, open(src_file2, "r") as f2, open(src_file3, "r") as f3, open("20k.txt", "r") as k:
        u1 = set(f1.read().splitlines())
        u2 = set(f2.read().splitlines())
        u3 = set(f3.read().splitlines())
        k_lines = set(k.read().splitlines())

        unused = k_lines - (u1+u2+u3)
        return(unused,len(unused))

