"""This package contains converter from num to string."""

from num2word import word


def convert(num):
    """Convert num into text."""
    try:
        text = word(num)
    except:
        return ("Make sure that, the number you passed "
                "doesn't contain any alphabet or special symbol!")
    return text
