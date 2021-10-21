# -*-coding:UTF-8 -*-
import os

def cut_txt(file_name, cut_methods_list):
    # 单个TXT文档处理，可以接收多个方法，
    # cut_methods_list: [("name", method), ...]
    # 以方法名作为键名，将其分词结果存储在字典中
    results = dict()
    with open(file_name, "r", encoding='utf-8') as f:
        for line in f:
            for pair in cut_methods_list:
                foo_name = pair[0]
                foo = pair[1]
                results[foo_name] = foo(line)
    return results


def write_results(file_name, results, delimiter='/', output_dir_prefix=''):
    for foo_name in results.keys():
        out_file_name = os.path.join(
            output_dir_prefix, 
            file_name + "." + foo_name + ".segmented")
        with open(out_file_name, 'w', encoding='utf-8') as out:
            out.write(
                delimiter.join(results[foo_name]))


def process_path(path, cut_methods_list):
    #传入某大学的文件路径， 对其各个标签项下的内容进行处理，文本分类后再重新写入（html.txt）
    ignore = ['href', '简介', 'segmented']
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
            print(file_name)
            
            # 获得各方法的分词结果：results
            yield file_name, cut_txt(file_name, cut_methods_list)

