from word2word import Word2word

en2fr = Word2word("en", "fr")
print(en2fr("apple"))
# out: ['pomme', 'pommes', 'pommier', 'tartes', 'fleurs']