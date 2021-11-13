from calc import *
from numpy.core.numeric import NaN

def print_PRF(gt, seg_list, method_name):
    print('{:<11}'.format(method_name + ':'), "/".join(seg_list))
    hits, len_truth, len_result, _ = calc_hits(gt, seg_list)
    P, R, F = calc_PRF(hits, len_truth, len_result)
    print('Hits:      ', hits)
    print('Precision: ', P)
    print('Recall:    ', R)
    print('F:         ', F)


def print_stat(foo_name, total_truth_cnt, total_result_cnt, total_hits):

    print('{} 分词结果：'.format(foo_name))
    print("{:<8} 分词总共的数目：{}".format("jieba", total_truth_cnt))
    print("{:<8} 分词总共的数目：{}".format(foo_name, total_result_cnt))
    print("{:<8} 分词正确的数目：{}".format(foo_name, total_hits))

    P, R, F = NaN, NaN, NaN

    if total_result_cnt != 0 and total_truth_cnt != 0:
        P, R, F = calc_PRF(total_hits, total_truth_cnt, total_result_cnt)

    print("准确率（P）：{:.5f} %".format(100 * P))
    print("回归率（R）：{:.5f} %".format(100 * R))
    print("F 值为：{}".format(F))
