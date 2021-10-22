import jieba
from FMM_BMM_trie import *   # 根据路径不同修改
from calc import *
from file_processing import * 

trainning_file_path = ["训练语料"]

wordlist, cnt, maxlen = load_wordlist('wordlist.dic')

FMM_cut = lambda line : FMM(line, wordlist, maxlen)
BMM_cut = lambda line : BMM(line, wordlist, maxlen)

methods = [
    ('jieba', jieba.lcut),
    ('FMM', FMM_cut),
    ('BMM', BMM_cut)
]

tot_hits = {'FMM': 0, 'BMM': 0}         # 统计 FMM/BMM 分词结果正确的个数
tot_result_cnt = {'FMM': 0, 'BMM': 0}   # 统计 FMM/BMM 分词结果的个数
tot_truth_cnt = 0                       # 统计 jieba 分词结果的个数

new_words = []

for path in trainning_file_path:
    # 对某一目录下结果进行处理
    for filename, results in process_path(path, methods):
        
        if len(results) == 0: continue
        
        truth = results['jieba']
        fmm = results['FMM']
        bmm = results['BMM']

        hits, len_truth, len_result, missmatches = calc_hits(truth, fmm)
        tot_hits['FMM'] += hits
        tot_result_cnt['FMM'] += len_result
        new_words += missmatches

        hits, len_truth, len_result, missmatches = calc_hits(truth, bmm)
        tot_hits['BMM'] += hits
        tot_result_cnt['BMM'] += len_result
        new_words += missmatches
        
        tot_truth_cnt += len_truth
        
        # 对同一个文档进行的 FMM 和 BMM 处理，虽然存在差异
        # 但大部分分词结果相同，故只将 FMM 分词结果存储

        write_results(filename, {'FMM': results["FMM"]}, '/')

import print_helper as helper

# 打印统计信息

helper.print_stat('FMM', tot_truth_cnt, tot_result_cnt['FMM'], tot_hits['FMM'])
helper.print_stat('BMM', tot_truth_cnt, tot_result_cnt['BMM'], tot_hits['BMM'])

# 将新词添加入词典
wordlist, cnt, maxlen = add_words(wordlist, cnt, maxlen, new_words)

save_wordlist('new_wordlist.dic', wordlist)
