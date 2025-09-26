def coleman_liau_index(text):
    letters = sum(c.isalpha() for c in text)
    words = len(text.split())
    sentences = text.count('.') + text.count('!') + text.count('?')

    if words == 0:
        return "Error: No words in text."

    L = (letters / words) * 100
    S = (sentences / words) * 100

    index = round(0.0588 * L - 0.296 * S - 15.8)

    if index < 1:
        return "Before Grade 1"
    elif index >= 16:
        return "Grade 16+"
    else:
        return f"Grade {index}"



