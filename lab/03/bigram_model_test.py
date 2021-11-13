from word_map import *
from dict_seg import *
from calc import *
from print_helper import *

import jieba

# trainning

model = BigramModel()

dict_seg = DictSeg()
dict_seg.load_wordlist("../02/new_wordlist.dic")

while True:
    # 从标准输入逐行读入训练语料
    line = input("Train material: ")
    line = line.strip()

    if line == '#':
        break

    l = jieba.lcut(line)
    
    # 如果是从文件读入分词的结果，则向 train 传入 split 后得到的列表
    # train 方法考虑了有标点符号的情况
    model.train(l)


while True:
    # 从标准输入逐行读入，可根据需要修改为从文件读入
    line = input()
    line = line.strip()
    
    if line == '#':
        break
    
    fmm = dict_seg.FMM(line)
    bmm = dict_seg.BMM(line)

    ground_truth = jieba.lcut(line)  # 'ground truth'
    
    print('{:<11}'.format("jieba"), "/".join(ground_truth))

    print('-' * 20)

    print_PRF(ground_truth, fmm, "FMM")

    print('-' * 20)

    print_PRF(ground_truth, bmm, "BMM")
    
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
    
    print('-' * 20)
    
    print_PRF(ground_truth, result, "Final")

