
def remove_punctuation(text):
    textwopunctuation = ""
    for c in text:
        if c not in [",","!",":",";"]:
           textwopunctuation = textwopunctuation+c
    return textwopunctuation

def convert_to_lowercase(text1):
    text2 = text1.lower()
    return text2

def tokenize_text(text3):
    return text3.split()

def sentence_tokenize(text4):
    return text4.split(".")



