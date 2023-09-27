def check_first_sentence_is_second(chstr, restr):
    if len(restr) == 0:
        return True
    chl = chstr.split(' ')
    rel = restr.split(' ')

    for el in rel:
        if chl.count(el) < rel.count(el):
            return False
    return True
