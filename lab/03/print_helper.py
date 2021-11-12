from calc import *

def print_PRF(gt, seg_list, method_name):
    print('{:<11}'.format(method_name + ':'), "/".join(seg_list))
    hits, len_truth, len_result, _ = calc_hits(gt, seg_list)
    P, R, F = calc_PRF(hits, len_truth, len_result)
    print('Hits:      ', hits)
    print('Precision: ', P)
    print('Recall:    ', R)
    print('F:         ', F)

