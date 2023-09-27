from collections import deque


class WordContextGenerator:
    def __init__(s, words, k):
        """
      :param words: Cписок слов
      :param k: Размер окна
      """
        s.w = words
        s.k = k

    def __iter__(s):
        s.output = deque()
        s.anchor = 0
        return s

    def __next__(s):
        if len(s.output) != 0:
            return s.output.popleft()
        elif s.anchor == len(s.w):
            raise StopIteration
        else:
            for i in range(max(0, s.anchor - s.k),
                           min(len(s.w), s.anchor + s.k + 1)):
                if i != s.anchor:
                    s.output.append((s.w[s.anchor], s.w[i]))
            s.anchor += 1
            return next(s)
