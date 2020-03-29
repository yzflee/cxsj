from collections import Counter
import re
#统计单词出现次数
file13=open(r"C:\Users\cyn\Desktop\data_search\result3.txt",'r',encoding='UTF-8')
a=file13.read()
def cal(data):
    data = data.lower().replace(',', '').replace('.', '')
     #替换除了n't这类连字符外的所有非单词字符和数字字符
    datalist = re.split(r'[\s\n]+', data)
    return Counter(datalist).most_common()

if __name__ == '__main__':
    dic = cal(a)
    for i in range(len(dic)):
        print('%15s  --->  出现了 %s 次' % (dic[i][0], dic[i][1]))

file13.close()
