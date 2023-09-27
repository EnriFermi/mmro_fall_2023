import sys
from collections import deque
from collections.abc import Iterable


class linearize:
    def __init__(s, obj):
        s.obj = obj

    def __iter__(s):
        s.stack = deque()
        s.str_b = deque()
        s.stack.append(iter(s.obj))
        return s

    def __next__(s):
        if len(s.stack) == 0 and len(s.str_b) == 0:
            raise StopIteration
        # Если буффер строк заполнен, то выводим из него
        if len(s.str_b) > 0:
            ch = s.str_b.popleft()
            return ch
        try:
            # Получаем очередной итератор из стека
            it = s.stack.pop()
            elem = next(it)  # first elem
            if type(elem) is str:
                for ch in elem:
                    s.str_b.append(ch)
                s.stack.append(it)
                return next(s)
            elif isinstance(elem, Iterable):
                s.stack.append(it)
                s.stack.append(iter(elem))
                return next(s)
            else:
                s.stack.append(it)
                return elem
        except StopIteration:
            return next(s)
