
import unittest
import pytest
import sys
sys.path.append(r"C:\Users\irink\projects\text_processor_project")

from text_processor.textcount import word_count, character_count, unique_words, average_word_length, find_occurrences


@pytest.mark.parametrize("a, expected", [
    ("Hello world", 2),
    ("a", 1),
    ("How many words are here?", 5),
    ("abc abc abc", 3),
    ("111, 222, 333", 3)
])
def test_word_count(a, expected):
    assert word_count(a) == expected
    
    
@pytest.mark.parametrize("a, expected", [
    ("Hello world", 11),
    ("a", 1),
    ("How many letters are here?", 26),
    ("abc abc abc", 11),
    ("111, 222, 333", 13)
])    
def test_character_count(a, expected):
    assert character_count(a) == expected


@pytest.mark.parametrize("a, expected", [
    ("Hello world", 2),
    ("a", 1),
    ("", 0),
    ("abc abcd abc", 2),
    ("111, 222, 333", 3),
    ("a ba ba ga la ma ga", 5)
])    
def test_unique_words(a, expected):
    assert unique_words(a) == expected



@pytest.mark.parametrize("a, expected", [
    ("Hello world", 5),
    ("a", 1),
    ("a a a?", 1),
    ("abc abcd abc", 3),
    ("11111, 2, 333333333", 5),
    ("a ba ba ga la ma ga", 2)
])    
def test_average_word_length(a, expected):
    assert average_word_length(a) == expected
    

    
@pytest.mark.parametrize("a, b, expected", [
    ("Hello world", "world", 1),
    ("a", "a", 1),
    ("This is a big big apple", "big", 2),
    ("abc abcd abc", "abc", 2),
    ("111, 222, 333", "", 0),
    ("", "a", 0)
])    
def test_find_occurences(a, b, expected):
    assert find_occurrences(a,b) == expected

