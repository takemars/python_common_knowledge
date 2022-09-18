import re

def cut_sentences_v1(sent):
    """
    the first rank of sentence cut
    """
    sent = re.sub('([。！？\?])([^”’])', r"\1\n\2", sent)  # 单字符断句符
    sent = re.sub('(\.{6})([^”’])', r"\1\n\2", sent)  # 英文省略号
    sent = re.sub('(\…{2})([^”’])', r"\1\n\2", sent)  # 中文省略号
    sent = re.sub('([。！？\?][”’])([^，。！？\?])', r"\1\n\2", sent)
    # 如果双引号前有终止符，那么双引号才是句子的终点，把分句符\n放到双引号后
    return sent.split("\n")

if __name__ == '__main__':
    a = re.sub('(\d{4})-(\d{2})-(\d{2})', r'\2-\3-\1', '2018-06-07')
    print(a) # '06-07-2018'
    a = re.sub('(\d{4})-(\d{2})-(\d{2})', r'\g<2>-\g<3>-\g<1>', '2018-06-07')
    print(a) # '06-07-2018'  # \2 和 \g<2> 指代的的都是前面的第二个分组