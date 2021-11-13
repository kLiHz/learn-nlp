from word_map import *
from dict_seg import *
from calc import *
from print_helper import *

import jieba
import os

def file_glob(path):
    """
    获得目录下的所有文件
    :param path: 目录名
    :return: 文件名（生成器）
    """
    ignore = ['href', '简介', 'segmented', '#']
    for root, subdirs, files in os.walk(path):
        for f in files:
            file_name = os.path.join(root, f)

            # 如果文件名含有某些特征，跳过
            should_pass = False
            for kw in ignore:
                if file_name.find(kw) != -1:
                    should_pass = True
                    break
            if should_pass: continue
                    
            yield file_name

# trainning

model = BigramModel()

with open('1998人民日报（分词）.txt', encoding='gbk') as f:
    for line in f:
        model.train(line.split())

dict_seg = DictSeg()
dict_seg.load_wordlist("../02/new_wordlist.dic")

tot_hits = {'FMM': 0, 'BMM': 0, "Result": 0}
tot_result_cnt = {'FMM': 0, 'BMM': 0, "Result": 0}
tot_truth_cnt = 0

for file_name in file_glob('../02/测试语料'):
    print(' - Processing:', file_name)
    with open(file_name) as f:
        for line in f:

            fmm = dict_seg.FMM(line)
            bmm = dict_seg.BMM(line)

            ground_truth = jieba.lcut(line)  # 'ground truth'
            
            # 由于分词结果中可能存在标点符号，先根据标点符号进行断句，再进行处理

            result = [] # 消歧结果

            i = 0
            j = 0

            while i < len(fmm) and j < len(fmm):
                k = i
                m = j
                
                while k < len(fmm) and fmm[k] not in punctuations:
                    k += 1
                
                while m < len(bmm) and bmm[m] not in punctuations:
                    m += 1
                
                l1 = fmm[i:k]
                l2 = bmm[j:m]

                word_map = WordMap(len("".join(l1)))
                
                word_map.add_to_word_map(l1)
                word_map.add_to_word_map(l2)

                i = k + 1
                j = m + 1

                combinations = list(word_map.all_possible_combinations_with_probability(model=model))

                max_prob = max(combinations, key=lambda c:c['p'])

                result += max_prob['l'][1:-1]

                if k < len(fmm):
                    result.append(fmm[k])

            hits, len_truth, len_result, _ = calc_hits(ground_truth, fmm)
            tot_hits['FMM'] += hits
            tot_result_cnt['FMM'] += len_result

            hits, len_truth, len_result, _ = calc_hits(ground_truth, bmm)
            tot_hits['BMM'] += hits
            tot_result_cnt['BMM'] += len_result

            hits, len_truth, len_result, _ = calc_hits(ground_truth, result)
            tot_hits['Result'] += hits
            tot_result_cnt['Result'] += len_result

            tot_truth_cnt += len_truth


# 打印统计信息

for class_name in tot_result_cnt.keys():
    print_stat(class_name, tot_truth_cnt, tot_result_cnt[class_name], tot_hits[class_name])
