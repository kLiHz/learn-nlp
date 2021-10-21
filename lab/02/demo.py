from FMM_BMM_trie import *
from calc import *

import jieba

wordlist, cnt, maxlen = load_wordlist('wordlist.dic')

while True:
    s = input().strip()
    if s == '#':
        break
    ground_truth = jieba.lcut(s)  # 'ground truth'
    fmm = FMM(s, wordlist, maxlen)
    bmm = BMM(s, wordlist, maxlen)

    print('jieba:     ', "/".join(ground_truth))

    print('-' * 20)

    print('FMM:       ', "/".join(fmm))
    hits, _ = calc_hits(ground_truth, fmm)
    print('Hits:      ', hits)
    print('Precision: ', hits / len(fmm))
    print('Recall:    ', hits / len(ground_truth))

    print('-' * 20)

    print('BMM:       ', "/".join(bmm))
    hits, _ = calc_hits(ground_truth, bmm)
    print('Hits:      ', hits)
    print('Precision: ', hits / len(bmm))
    print('Recall:    ', hits / len(ground_truth))
