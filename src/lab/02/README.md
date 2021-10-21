# 自然语言处理：实验二


{{#include ../misc/author-info.html}}

日期： 2021 年 9 月 29 日

## 摘要


## 目录

## 一、实验内容

实验内容：对语料库的文本进行分词并存储。

分别采用正向最大匹配算法、逆向最大匹配算法进行分词。

以 [jieba](https://github.com/fxsjy/jieba) 分词的分词结果作为标准语料，计算P、R、F值。


## 二、实验原理

包含：存在的主要问题，用什么方法解决，原理是什么？

基于词典的切分方法


最大匹配法（Maximum Matching, MM）

有词典切分，机械切分

- 正向最大匹配算法（Forward MM, FMM）
- 逆向最大匹配算法（Backward MM, BMM）
- 双向最大匹配算法（Bi-directional MM）

句子 \\(S = c_1 c_2 \cdots c_n\\)：句子由若干字符 \\(c\\) 组成。

假设词 \\(w_i = c_1c_2 \cdots c_m\\)，其中 \\(m\\) 为词典中最长词的字数。


## 三、整体框架

包含整体框图，各主要模块的功能。

图表都需要 **带编号**

## 四、主要程序模块

考虑到可能会涉及大量词语的存储与检索，尝试使用将词库载入并存储于自己实现的 Trie 字典树结构中。

为了简便起见，使用 Python 中的字典结构模拟节点对象。

[my_trie.py](./my_trie.py)

```python
{{#include my_trie.py}}
```

使用示例：

[trie_test.py](./trie_test.py)

```python
{{#include trie_test.py}}
```

从文件中加载字典到 Trie 树，并进行最大正向匹配、最大逆向匹配：

[FMM_BMM_trie.py](./FMM_BMM_trie.py) （使用 Python 内建的 set 类型：[FMM_BMM.py](./FMM_BMM.py)）

```python
{{#include FMM_BMM_trie.py}}
```

计算 P、R、F 值：

[calc.py](./calc.py)

```python
{{#include calc.py}}
```


交互式分词程序：

[demo.py](./demo.py)

```python
{{#include demo.py}}
```

详细介绍各个主要模块的功能及实现流程。

## 五、实验结果

详细分析实验结果，除了包含定量评价，还要有定性评价。
对存在的问题，要着重剖析。

## 六、总结

除了对整个实验进行概要总结，如果有程序亮点，可以在这阐述。

## 参考文献

如有参考文献，请附上。



