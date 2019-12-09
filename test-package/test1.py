import jieba
ss = jieba.cut('这是一个句子',cut_all=True)
print('/'.join(ss))