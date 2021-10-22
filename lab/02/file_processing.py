# -*-coding:UTF-8 -*-
import os
import time

def cut_txt(file_name, cut_methods_list):
    """
    单个TXT文档处理，可以接收多个方法，
    :param file_name:   要处理的文件名
    :param cut_methods_list: 类似如下的列表 [("name", method), ...]
    :return: 存储分词结果的字典，以方法名作为键名
    """
    results = dict()
    elapsed_time = 0
    with open(file_name, "r", encoding='utf-8') as f:
        for line in f:
            for pair in cut_methods_list:
                foo_name = pair[0]
                foo = pair[1]
                start = time.time()
                results[foo_name] = foo(line.strip())
                end = time.time()
                elapsed_time += (end - start)

    return results, elapsed_time


def write_results(file_name, results, delimiter='/', output_dir_prefix=''):
    """
    将分词结果写出到文件
    """
    for foo_name in results.keys():
        out_file_name = os.path.join(
            output_dir_prefix, 
            file_name + "." + foo_name + ".segmented")
        with open(out_file_name, 'w', encoding='utf-8') as out:
            out.write(
                delimiter.join(results[foo_name]))


def process_path(path, cut_methods_list):
    """
    对目录下的所有文件进行处理
    :param path: 目录名
    :param cut_methods_list: 要采用的分词方法的列表
    :return: 文件名及对应结果的生成器
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

            # 当前正在处理的文件
            print(' - Processing:', file_name)
            
            # 获得各方法的分词结果：results
            
            results, t = cut_txt(file_name, cut_methods_list)

            yield file_name, results, t 

