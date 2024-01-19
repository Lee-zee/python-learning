# import sys
# script,encoding,error = sys.argv 

# def main(language_file,encoding,errors):
#     line = language_file.readline()

#     if line:
#         print_line(line,encoding,errors)
#         return main(language_file,encoding,errors)
    
# def print_line(line,encoding,errors):
#     next_lang = line.strip()
#     raw_bytes = next_lang.encode(encoding,errors = errors)
#     cooked_string = raw_bytes.decode(encoding,errors = errors)

#     print(raw_bytes,"<==>",cooked_string)

# languages = open("./public/text/languages.txt",encoding="utf-8")

# main(languages,encoding,error)

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)