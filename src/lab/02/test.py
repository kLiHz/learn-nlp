import jieba
from FMM_BMM_trie import *   # 根据路径不同修改
from calc import *
from file_processing import * 

wordlist, cnt, maxlen = load_wordlist('new_wordlist.Dic')

print("------------------训练后---------------------")

FMM_cut = lambda line : FMM(line, wordlist, maxlen)
BMM_cut = lambda line : BMM(line, wordlist, maxlen)

methods = [
    ('jieba', jieba.lcut),
    ('FMM', FMM_cut),
    ('BMM', BMM_cut)
]

test_file_path = ["测试语料"]

tot_hits = {'FMM': 0, 'BMM': 0}
tot_result_cnt = {'FMM': 0, 'BMM': 0}
tot_truth_cnt = 0

for path in test_file_path:
    # 对某一目录下结果进行处理
    for filename, results in process_path(path, methods):
        
        if len(results) == 0: continue

        truth = results['jieba']
        fmm = results['FMM']
        bmm = results['BMM']

        hits, len_truth, len_result, _ = calc_hits(truth, fmm)
        tot_hits['FMM'] += hits
        tot_result_cnt['FMM'] += len_result

        hits, len_truth, len_result, _ = calc_hits(truth, bmm)
        tot_hits['BMM'] += hits
        tot_result_cnt['BMM'] += len_result
        
        tot_truth_cnt += len_truth

import print_helper as helper

# 打印统计信息

helper.print_stat('FMM', tot_truth_cnt, tot_result_cnt['FMM'], tot_hits['FMM'])
helper.print_stat('BMM', tot_truth_cnt, tot_result_cnt['BMM'], tot_hits['BMM'])
