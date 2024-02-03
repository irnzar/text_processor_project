def word_count(text):
    return len(text.split())


def character_count(text):
    n = 0
    for c in text:
        n += 1
    return n

def unique_words(text):
    l1 = text.split()
    s1 = set(l1)
    l1 = list(s1)
    return len(s1)

def average_word_length(text):
    l1 = text.split()
    word_count = len(l1)
    letter_count = 0
    for c in text:
        if c not in [",","!",":",";"," "]:
           letter_count+=1
    avg_word_length = round (letter_count/word_count,0)
    return avg_word_length

def find_occurrences (text, keyword):
    l1 = text.split()
    n = 0
    for i in range(len(l1)):
        if l1[i] == keyword:
            n +=1
    return n    
    

