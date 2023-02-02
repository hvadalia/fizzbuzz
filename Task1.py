
def leetcode_rules(src_file, dest_file):
    with open(src_file, "r") as src, open(dest_file,"w") as dest:
        text = src.read()
        rules_dict = {"o":"0", "O":"0", "a":"4", "A":"4", "e":"3", "E":"e", "i":"1", "I":"1"}

        text = text.translate(str.maketrans(rules_dict))
        dest.write(text)

leetcode_rules("Book1.txt","output.txt")
