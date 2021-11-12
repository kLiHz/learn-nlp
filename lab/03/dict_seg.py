
class DictSeg:
    """
    词典分词
    """
    wordlist = set()
    maxlen = 0      # maxlen 为字典中最长词的长度
    cnt = 0

    def load_wordlist(self, filename):
        self.wordlist = set()
        self.maxlen = 0
        self.cnt = 0
        with open(filename) as f:
            # 判断文件首行是否为指定的 'magic code'
            if f.readline().strip() == '@Lexicon':
                for line in f:
                    word = line.split()[1]
                    self.maxlen = max(self.maxlen, len(word))
                    self.cnt += 1
                    self.wordlist.add(word)


    def add_words(self, new_words):
        for w in new_words:
            w = w.strip()
            if len(w) == 0:
                continue
            if w.startswith("-") or w.startswith("."):
                # 排除可能的特殊符号串，如“----------”
                continue
            if w.isdigit():
                # 同理，排除掉特殊情况，使得字典更具有普遍性
                continue
            
            if w not in self.wordlist:
                self.cnt += 1
                self.maxlen = max(len(w), self.maxlen)
                self.wordlist.add(w)


    def save_wordlist(self, filename):
        with open(filename, "w", encoding='utf-8') as out:
            out.write('@Lexicon\n')
            cnt = 0
            for w in self.wordlist:
                cnt += 1
                out.write(str(cnt) + ' ' + w + '\n')


    def FMM(self, sentence):
        maxlen = max(1, self.maxlen)
        tokens = []
        i = 0
        while i < len(sentence):
            n = len(sentence) - i # 未被切分的字串长度
            m = min(maxlen, n)
            w = sentence[i:i+m]
            while len(w) > 1:
                if w in self.wordlist:
                    break
                else:
                    w = w[0:-1]
            tokens.append(w)
            i += len(w)
        return tokens


    def BMM(self, sentence):
        maxlen = max(1, self.maxlen)
        tokens = []
        i = len(sentence)
        while i >= 1:
            n = i # 未被切分的字串长度
            m = min(maxlen, n)
            w = sentence[i-m:i]
            while len(w) > 1:
                if w in self.wordlist:
                    break
                else:
                    w = w[1:]
            tokens.append(w)
            i -= len(w)
        tokens.reverse()
        return tokens


