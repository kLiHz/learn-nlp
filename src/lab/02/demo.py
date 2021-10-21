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
    hits, len_truth, len_result, _ = calc_hits(ground_truth, fmm)
    P, R, F = calc_PRF(hits, len_truth, len_result)
    print('Hits:      ', hits)
    print('Precision: ', P)
    print('Recall:    ', R)
    print('F:         ', F)

    print('-' * 20)

    print('BMM:       ', "/".join(bmm))
    hits, len_truth, len_result, _ = calc_hits(ground_truth, bmm)
    P, R, F = calc_PRF(hits, len_truth, len_result)
    print('Hits:      ', hits)
    print('Precision: ', P)
    print('Recall:    ', R)
    print('F:         ', F)
