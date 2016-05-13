import itertools as it
import string

def segmentText(text):
    text = text.strip(' \n,.')

    # ========= 1 ========================

    terms = []
    _ = 0
    rmchar = string.punctuation + string.whitespace
    for c in range(1, text.__len__()):
        if (text[c] in rmchar):
            if (text[c] not in '/\\+('):
                if (text[_:c+1].strip(rmchar) != ''):
                    terms.append(text[_:c+1])
                    _ = c + 1
    if (text[_:c + 1].strip(rmchar) != ''):
        terms.append(text[_:c + 1])

    ls = []
    for cb in list(it.combinations(range(len(terms) - 1), 2)):
        term1 = ''.join(terms[:cb[0] + 1]).strip()
        term2 = ''.join(terms[cb[0] + 1:cb[1] + 1]).strip()
        term3 = ''.join(terms[cb[1] + 1:]).strip()
        ls.append([term1, term2, term3])

    # ========= 2 ========================
    # ls = []
    # for cb in list(it.combinations(range(len(terms) - 1), 2)):
    #     term1 = ' '.join(terms[:cb[0]+ 1]).strip()
    #     term2 = ' '.join(terms[cb[0]+1:cb[1]+1]).strip()
    #     term3 = ' '.join(terms[cb[1]+1:]).strip()
    #     _ = (1 if term1[-1] in string.punctuation else 0) + \
    #         (1 if term2[-1] in string.punctuation else 0) + \
    #         (1 if term3[-1] in string.punctuation else 0)
    #     if (_ >= 2):
    #         ls.append([term1, term2, term3])

    return ls
