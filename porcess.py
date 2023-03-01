import jieba
import re
jieba.add_word('还行')
comments = open('raw_comments.txt', 'r', encoding='utf-8')
save_file = open('data.txt','a',encoding='utf-8')
stopwords_file = open('stopwords.txt', 'r', encoding='utf-8')
stopwordlist = [words.strip() for words in stopwords_file.readlines()]
for line in comments.readlines():
    need = []
    wordlist = jieba.cut(str(line), use_paddle=True)  # 精确模式
    for x in wordlist:
        if (x not in stopwordlist):
            need.append(x)
    wl = " ".join(need)
    wl = re.sub('\d+', '', wl)
    rew = wl.replace('力荐','1',1).replace('推荐','1',1).replace('还行','1',1).replace('较差','0',1).replace('很差','0',1)
    new_line = rew.strip()
    print(new_line)
    if new_line == '':
        pass
    elif new_line[0]=='0' or new_line[0]=='1':
        save_file.write('\n')
        save_file.write(new_line)
    else:
        save_file.write(' ')
        save_file.write(new_line)

comments.close()
save_file.close()