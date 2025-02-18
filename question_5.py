punctuation_remove = (",.!?")
punctuation_space = ("'")

def find_C_jeb_words(filename):
    """
    Finds all the words starting with C and ending in jeb in the file
    :param filename: the name of the file
    :return: None
    """
    with open(filename, "r") as f:
        # this makes it go line by line
        count = 0
        for line in f:
            for p in punctuation_remove:  #removes punctuation
                line = line.replace(p,"")
            for p in punctuation_space:  #replaces punctuation with a space
                line = line.replace(p,"")
            words = line.split() #recognises the line as individual words

            for word in words:
                if word.lower().startswith("c") and word.lower().endswith("jeb"):
                    count += 1
    return count
print(find_C_jeb_words("input.txt"))




