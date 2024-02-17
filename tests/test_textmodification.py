import unittest
import pytest
import sys
sys.path.append(r"C:\Users\irink\projects\text_processor_project")

from text_processor.textmodification import remove_punctuation, convert_to_lowercase, tokenize_text, sentence_tokenize

@pytest.mark.parametrize("a, expected", [
    ("Hello world!", "Hello world"),
    ("a: a", "a a"),
    ("How many words are here?", "How many words are here"),
    ("", ""),
    ("111, 222, 333", "111 222 333")
])
def test_remove_punctuation(a, expected):
    assert remove_punctuation(a) == expected



@pytest.mark.parametrize("a, expected", [
    ("Hello world!", "hello world!"),
    ("A: A", "a: a"),
    ("an APPle", "an apple"),
    ("How Many Words Are Here?", "how many words are here?"),
    ("", ""),
    ("111, 222, 333", "111, 222, 333")    
])
def test_convert_to_lowercase(a, expected):
    assert convert_to_lowercase(a) == expected
    

@pytest.mark.parametrize("a, expected", [
    ("Hello world!", ["Hello","world!"]),
    ("A: A", ["A:","A"]),
    ("an APPle", ["an","APPle"]),
    ("How to split this by words?", ["How","to","split","this","by","words?"]),
    ("", []),
    ("111, 222, 333", ["111,","222,","333"])    
])
def test_tokenize_text(a, expected):
    assert tokenize_text(a) == expected
    
@pytest.mark.parametrize("a, expected", [
    ("Hello world!", ["Hello world!"]),
    ("A.A", ["A","A"]),
    ("A pear. An apple", ["A pear"," An apple"]),
    ("How to split this. By sentences", ["How to split this"," By sentences"]),
    ("", [""]),
    ("111, 222. 333", ["111, 222"," 333"])    
])
def test_sentence_tokenize(a, expected):
    assert sentence_tokenize(a) == expected