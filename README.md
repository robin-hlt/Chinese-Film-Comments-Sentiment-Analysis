# Chinese-Film-Comments-Sentiment-Analysis
A course experiment in Social Networking of NUIST (School of AI)

author:Robin Hua  
version:1.0

In this experiment, LSTM is used to analyse the sentiment of film comments which are collected from [douban](https://movie.douban.com/). All codes are implemented in Python3.7. Anaconda is used to manage the virtual environments.

The structure of the folder：

>--Chinese-Film-Comments-Sentiment-Analysis    
>>--model #save the trained model  
>>get_comments.py #get film comments from douban  
>>process.py #preprocess the data  
>>train_test_spilit.py  
>>train.py #train the LSTM model  
>>predict.py #predict the new comments with the trained model  
>>raw_comments.txt #raw data got after running get_comments.py  
>>data.txt #data got after preprocess  
>>training_set.txt #data splited from data.txt  
>>validation_set.txt #data splited from data.txt  
>>stopwords.txt  
>>w2v_model.bin # pretrained word2vector model  
   
For detailed Chinese interpretation, please refer to .
