punctuations = {',', '，', ';', '；', '。', '!', '！', '?', '？', '（', '）', '—', '——', '：'}

ignore_characters = {'"', '\'', '“', '”', '‘', '’', '：', '《','》', '『', '』', '、'}

BOS = '<BOS>'
EOS = '<EOS>'

NUMERAL = '<num>'

def bigram_pairing(seg_list):
    """
    将分词得到的列表进行二元文法匹配，得到二元文法词组列表
    """
    former_word = BOS

    for word in seg_list:
        if word in ignore_characters:
            continue

        if word in punctuations:
            yield (former_word, EOS)
            former_word = BOS
            continue
        else:
            word = NUMERAL if word.isdigit() else word
            yield (former_word, word)
            former_word = word
    
    if former_word != BOS:
        yield (former_word, EOS)


class BigramModel:

    bi_cnt = {}     # bi-gram count: A `dict` of `dict`s
    uni_cnt = {}    # uni-gram (word frequency) count: A dict
    
    def __init__(self) -> None:
        pass


    def train(self, seg_list):

        def bigram_train():
            """
            使用 **二元元组的列表** 进行统计，训练二元语法模型
            """
            for t in bigram_pairing(seg_list):
                w1, w2 = t
                if w1 not in self.bi_cnt:
                    self.bi_cnt[w1] = dict()

                if w2 not in self.bi_cnt[w1]:
                    self.bi_cnt[w1][w2] = 0

                self.bi_cnt[w1][w2] += 1

        def unigram_train():
            """
            使用 **词元列表** 进行词频统计
            """
            for word in seg_list:
                
                if word in ignore_characters or word in punctuations:
                    # 排除不需要的标点符号
                    continue
                
                if word.isdigit():
                    self.uni_cnt[NUMERAL] = self.uni_cnt.get(NUMERAL, 0) + 1
                else:
                    self.uni_cnt[word] = self.uni_cnt.get(word, 0) + 1
        
        bigram_train()
        unigram_train()


    def calc_probabilty(self, t, smooth="NONE"):
        """
        使用 MLE 计算二元元组的概率
        """
        w1, w2 = t

        w1 = NUMERAL if w1.isdigit() else w1        
        w2 = NUMERAL if w2.isdigit() else w2

        c_w1 = self.uni_cnt.get(w1, 0)
        
        if smooth == "NONE":
            if c_w1 == 0:
                # w1 not existing
                return 0
            else:
                # w1 existing
                c_w1w2 = self.bi_cnt[w1].get(w2, 0)
                return c_w1w2 / c_w1
        
        elif smooth == "ADD_ONE":
            if c_w1 == 0:
                # w1 not existing
                return 1 / len(self.uni_cnt)
            else:
                # w1 existing
                c_w1w2 = self.bi_cnt[w1].get(w2, 0)
                return (c_w1w2 + 1) / (c_w1 + len(self.uni_cnt))

        return 0
