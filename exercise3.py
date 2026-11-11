def average(numbers):
    """Average of a list. An empty list has average 0"""
    return 0 if len(numbers) == 0 else sum(numbers) / len(numbers) 


def first_word(text):
    """The first word of the text, or "" if the text is empty"""
    return text.split()[0] if text.split() else ""


def percent(part, total):
    """part as a percentage of total. If total is 0, the result is 0"""
    return 0 if total == 0 else part / total * 100
