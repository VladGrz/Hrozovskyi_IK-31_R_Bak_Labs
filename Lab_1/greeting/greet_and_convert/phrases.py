"""This module has questions for user."""


def get_name():
    """Asks user`s name."""
    name = input("Tape your name: ")
    return name


def say_hi(name="stranger"):
    """Greets user."""
    print(f"Hello, {name}")


def get_num():
    """Asks user`s number."""
    num = input("Which number you want to convert into text: ")
    return num
