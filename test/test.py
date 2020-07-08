import pytest
import sys
sys.path.insert(1, "../pysquat")
from ossquat import OSSquat
import logging
logging.basicConfig(level=logging.DEBUG)

def test_get_repeated_characters_two_characters():
    squat = OSSquat(package_name="reequest")
    repeated_chars = list(squat.get_repeated_characters())
    logging.info(f"""repeated characters: {repeated_chars[0][0]}, number of occurences: {repeated_chars[0][1]}""")
    assert repeated_chars[0][0] == 'e'
    assert repeated_chars[0][1] == 2

def test_get_repeated_characters_three_characters():
    squat = OSSquat(package_name="reeequest")
    repeated_chars = list(squat.get_repeated_characters())
    logging.info(f"""repeated characters: {repeated_chars[0][0]}, number of occurences: {repeated_chars[0][1]}""")
    assert repeated_chars[0][0] == 'e'
    assert repeated_chars[0][1] == 3

def test_get_repeated_characters_different_characters():
    squat = OSSquat(package_name="reeequestii")
    repeated_chars = list(squat.get_repeated_characters())
    logging.info(f"""repeated characters: {repeated_chars[1][0]}, number of occurences: {repeated_chars[1][1]}""")
    assert repeated_chars[1][0] == 'i'
    assert repeated_chars[1][1] == 2

def test_get_swapped_words():
    squat = OSSquat(package_name="python-nmap")
    swap_words = squat.get_swapped_words()
    logging.info(f"Swap words: {swap_words}")
    assert swap_words == "nmap-python"
