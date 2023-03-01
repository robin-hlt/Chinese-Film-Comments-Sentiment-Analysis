import pandas as pd
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import numpy as np
from gensim.models import KeyedVectors
from keras.models import Sequential
from keras.layers import Embedding, Flatten, Dense, LSTM
import matplotlib.pyplot as plt
train_df = pd.read_csv("./training_set.txt",
                       sep="\t", header=None, names=["label", "sentence"])
val_df = pd.read_csv("./validation_set.txt",
                     sep="\t", header=None, names=["label", "sentence"])
df = pd.concat([train_df,val_df])
print(df)
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
print(word_index)
labels = np.array(df['label'])
indices = np.arange(data.shape[0])
np.random.shuffle(indices)
data = data[indices]
labels = labels[indices]
training_samples = int(len(indices) * .8)
validation_samples = len(indices) - training_samples
X_train = data[:training_samples]
y_train = labels[:training_samples].astype('float64')
X_valid = data[training_samples: training_samples + validation_samples]
y_valid = labels[training_samples: training_samples + validation_samples].astype('float64')
zh_model = KeyedVectors.load_word2vec_format('./w2v_model.bin',binary=True)
embedding_dim = len(zh_model[next(iter(zh_model.key_to_index))])
embedding_matrix = np.random.rand(max_words, embedding_dim)
embedding_matrix = (embedding_matrix - 0.5) * 2
for word, i in word_index.items():
    if i < max_words:
        try:
          embedding_vector = zh_model.get_vector(word)
          embedding_matrix[i] = embedding_vector
        except:
          pass

#define model
units = 32

model = Sequential()
model.add(Embedding(max_words, embedding_dim))
model.add(LSTM(units))
model.add(Dense(1, activation='sigmoid'))
model.summary()
model.layers[0].set_weights([embedding_matrix])
model.layers[0].trainable = False
model.compile(optimizer='rmsprop',
             #设定损失函数
             loss='binary_crossentropy',
             metrics=['acc'])
history = model.fit(X_train, y_train,
            epochs=10,
            batch_size=32,
            validation_data=(X_valid.astype('float64'),y_valid.astype('float64'))
            )
model.save('./model/lstm_chekpoint.h5')
acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(acc) + 1)
plt.figure()
#显示训练集和验证集的精确度
plt.plot(epochs, acc, label='Training acc')
plt.plot(epochs, val_acc, label='Validation acc')
plt.plot(epochs, loss, label='Training loss')
plt.title('Training and validation accuracy')
plt.legend()
plt.show()