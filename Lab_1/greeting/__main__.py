"""This module defines default execution."""

from greeting.greet_and_convert.phrases import get_name, get_num, say_hi
from greeting.greet_and_convert.converter import convert

if __name__ == "__main__":
    name = get_name()
    say_hi(name)
    num = get_num()
    word = convert(num)
    print(word)
