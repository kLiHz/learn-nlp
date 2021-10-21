from my_trie import *

def load_wordlist(filename):
    wordlist = { 'c': '', 'children':dict(), 'cnt': 0 }
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