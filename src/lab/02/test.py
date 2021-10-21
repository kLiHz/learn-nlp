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


test_file_path = ["重庆大学", "西华大学"]

tot_hits = {'FMM': 0, 'BMM': 0}
tot_result_cnt = {'FMM': 0, 'BMM': 0}
tot_truth_cnt = 0

for path in test_file_path:
    # 对某一目录下结果进行处理
    for filename, results in process_path(path, methods):
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

print('FMM 分词结果：')
print("jieba 分词总共的数目:", tot_truth_cnt)
print("FMM   分词总共的数目:", tot_result_cnt['FMM'])
print("FMM   分词正确的数目：", tot_hits['FMM'])

P, R, F = calc_PRF(tot_hits['FMM'], tot_truth_cnt, tot_result_cnt['FMM'])

print("准确率（P）：{:.5f} %".format(100 * P))
print("回归率（R）：{:.5f} %".format(100 * R))
print("F 值为：{}".format(F))


print('BMM 分词结果：')
print("jieba 分词总共的数目:", tot_truth_cnt)
print("BMM   分词总共的数目:", tot_result_cnt['BMM'])
print("BMM   分词正确的数目：", tot_hits['BMM'])

P, R, F = calc_PRF(tot_hits['BMM'], tot_truth_cnt, tot_result_cnt['BMM'])

print("准确率（P）：{:.5f} %".format(100 * P))
print("回归率（R）：{:.5f} %".format(100 * R))
print("F 值为：{}".format(F))
