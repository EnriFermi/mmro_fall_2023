def find_word_in_circle(circle, word):
    if not len(circle):
        return -1
    circle_e = circle * (len(word) // len(circle) + 2)
    res = circle_e.find(word)
    if res != -1:
        return res % len(circle), 1
    else:
        res = circle_e[::-1].find(word)
        if res != -1:
            return (len(circle_e) - res - 1) % len(circle), -1
        else:
            return -1
