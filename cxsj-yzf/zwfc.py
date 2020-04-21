import jieba
import codecs, sys
from string import punctuation
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')
# 定义要删除的标点等字符
add_punc = '，。、【 】 “”：；（）《》‘’{}？！⑦()、%^>℃：.”“^-——=&#@￥'
all_punc = punctuation + add_punc
# 指定要分词的文本
f = codecs.open('C:/Users/lem/Desktop/data.txt', 'r', encoding="utf8")
# 指定分词结果的保存文本
target = codecs.open("C:/Users/lem/Desktop/out.txt", 'w', encoding="utf8")
print ('open files')
line_num = 1
line = f.readline()
while line:
    print('---- processing ', line_num, ' article----------------')
    line_seg = " ".join(jieba.cut(line))
    testline = line_seg.split(' ')
    te2 = []
    for i in testline:
        te2.append(i)
        if i in all_punc:
            te2.remove(i)
    line_seg2 = " ".join(jieba.cut(''.join(te2)))
    target.writelines(line_seg2)
    line_num = line_num + 1
    line = f.readline()
f.close()
target.close()
exit()
