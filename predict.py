from keras.models import load_model
import jieba
import pandas as pd
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
train_df = pd.read_csv("./training_set.txt",
                       sep="\t", header=None, names=["label", "sentence"])
val_df = pd.read_csv("./validation_set.txt",
                     sep="\t", header=None, names=["label", "sentence"])
df = pd.concat([train_df,val_df])
#设置每条评论保留的单词数量
maxlen = 100
#设置全局字典里要保留的单词数量
max_words = 10000
#创建分词器对象
tokenizer = Tokenizer(num_words=max_words)
#调用fit_on_texts方法，传递用以训练的文本列表
tokenizer.fit_on_texts(df['sentence'].fillna(""))
#调用texts_to_sequences方法，将文本列表转换为序列列表
sequences = tokenizer.texts_to_sequences(df['sentence'].fillna(""))
data = pad_sequences(sequences, maxlen=maxlen)
word_index = tokenizer.word_index
model = load_model('./model/lstm_chekpoint.h5')
sentence1 = '过了这么些年 这种电视剧就是重新翻新装裱过的手撕鬼子剧 这两年太多太多这种剧了 真的很无聊'
sentence2 = '只要尺度放开，中国也是可以拍出很精彩的剧的！张译和张颂文两位演技派把一正一邪的形象在黑社会帽子影响下的演变演绎了出来，非常精彩，人物都有血有肉，追剧追剧'
def show_pred(sentence):
    input = np.zeros((100,))
    i = -1
    for x in jieba.cut(sentence):
        if x in word_index.keys():
            input[i] = word_index[x]
            i -= 1
        else:
            input[i] = 0
            i -= 1
    label = model.predict(input.reshape(1, -1))
    if label < 0.5:
        print('positive')
    else:
        print('negtive')
show_pred(sentence1)
show_pred(sentence2)
