from my_trie import *

def load_wordlist(filename):
    wordlist = dict()
    maxlen = 0
    cnt = 0
    with open(filename) as f:
        if f.readline().strip() == '@Lexicon':
            for line in f:
                word = line.split()[1]
                maxlen = max(maxlen, len(word))
                insert(wordlist, word)
                cnt += 1
    return wordlist, cnt, maxlen


def add_words(wordlist, cnt, maxlen, new_words):
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
        cnt += 1
        maxlen = max(len(w), maxlen)
        insert(wordlist, w)
    return wordlist, cnt, maxlen


def save_wordlist(filename, wordlist):
    with open(filename, "w", encoding='utf-8') as out:
        out.write('@Lexicon\n')
        cnt = 0
        for w in traverse(wordlist):
            cnt += 1
            out.write(str(cnt) + ' ' + w + '\n')


def FMM(sentence, wordlist, maxlen):
    maxlen = max(1, maxlen)
    tokens = []
    i = 0
    while i < len(sentence):
        n = len(sentence) - i # 未被切分的字串长度
        m = min(maxlen, n)
        w = sentence[i:i+m]
        while len(w) > 1:
            if find(wordlist, w):
                break
            else:
                w = w[0:-1]
        tokens.append(w)
        i += len(w)
    return tokens


def BMM(sentence, wordlist, maxlen):
    maxlen = max(1, maxlen)
    tokens = []
    i = len(sentence)
    while i >= 1:
        n = i # 未被切分的字串长度
        m = min(maxlen, n)
        w = sentence[i-m:i]
        while len(w) > 1:
            if find(wordlist, w):
                break
            else:
                w = w[1:]
        tokens.append(w)
        i -= len(w)
    tokens.reverse()
    return tokens
