# -*- coding: utf-8 -*-
"""
Created on Mon May 22 11:45:29 2017

@author: 30216
"""
import sys
sys.path.append("C:\\Python27\\Lib\\site-packages")
from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
from gensim import corpora, models
from textblob import TextBlob
from os.path import basename
import nltk
import numpy as np
import pandas as pd
import gensim
import argparse
import re

class TextAnalytics(object):
    
    def clean_tweet(self, data):
        raw_text = " ".join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(\d+)|(\b\w{1,2}\b)", " ", data).split())
        text = raw_text.replace(","," ")
        return text.encode('utf-8')
        
    def clean_review(self,data):
        raw_text = " ".join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(\d+)|(\b\w{1,2}\b)", " ", data).split())
        text = raw_text.replace(" 39 ","").replace("quot","").replace(","," ")
        return text.encode('utf-8')
    
    def get_data_sentiment(self, tweet):
        
        # create TextBlob object of passed tweet text
        
        analysis = TextBlob(self.clean_tweet(tweet))
        if(len(analysis) != 0):
            
        # set sentiment
            if analysis.sentiment.polarity > 0:
                return 'positive'
            elif analysis.sentiment.polarity == 0:
                return 'neutral'
            else:
                return 'negative'
        else:
            return 'No valid sentiment from the tweet'
    
    def get_data_topic(self, review):
    
        texts = []
        #print(review)
        tokenizer = RegexpTokenizer(r'\w+')
        
        stop_word = []
        f = open("stop_words.txt","r")
        stop_word = f.read()

        # creating lemmatization word list
        lemma = WordNetLemmatizer()
    
        raw = review.lower()
        raw_text = self.clean_review(raw)
        #print raw_text
        if(len(raw_text) != 0):
            
            tokens = tokenizer.tokenize(raw_text)
        
            # remove stop words from tokens
            stopped_tokens = [i for i in tokens if not i in stop_word]
            if(len(stopped_tokens) != 0):
                # stem token
                stemmed_tokens = [lemma.lemmatize(i) for i in stopped_tokens]
                if(len(stemmed_tokens) != 0):
                    #print(stemmed_tokens)
        
                # add tokens to list
                    texts.append(stemmed_tokens)
        
                    dictionary = corpora.Dictionary(texts)
                #dictionary = []
                #print(dictionary)
        

            # convert tokenized documents into a document-term matrix
                    corpus = [dictionary.doc2bow(text) for text in texts]
            #print corpus
        # generate LDA model
                    np.random.seed(1000)

                    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=3, id2word = dictionary, passes=20)

        #print(ldamodel.print_topics(num_topics=1, num_words=3))
                    rev_topics = ldamodel.print_topics(num_topics=1, num_words=3)
        
                    return rev_topics[0][1]
                else:
                    return "No topic can be identified"
            else:
                return "Cleaned data has no keywords"
        else:
            return "Text has no information"
    
    def get_data(self, query):
  
        parsed_data = []
        
        content = query['text']
        
        for i in range(0,len(content)):
        
            content_data = {}
            content_data['text'] = content[i]        
            content_data['sentiment'] = self.get_data_sentiment(content[i])
            content_data['topics'] = self.get_data_topic(content[i])
            parsed_data.append(content_data)
        return parsed_data
        
final = "Text"+","+"Sentiment"+","+"Topics"
print final.decode('ascii','ignore')

#ap = argparse.ArgumentParser()
#ap.add_argument('--file',help='file input')
#args = ap.parse_args()

def main():
    
    tm = TextAnalytics()
    words = set(nltk.corpus.words.words())
    #file_path = "D:\\POC\\Vision 2017\\Review website\\aviva_review.csv"
    #file_path = "D:\\POC\\Vision 2017\\Sentiment and Topic modelling\\Taj_review.csv"
    #file_path = args["file"]
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required = True,help = "Path to the file")
    args = vars(ap.parse_args())
    file_name = basename(args["file"])
    regexp = re.compile(r'review')
        
    if regexp.search(file_name):
        extracted_data_new = pd.read_csv(args["file"])
        extracted_data_new.columns = extracted_data_new.columns.str.strip()
        data = tm.get_data(query = extracted_data_new)
        fin_out = pd.DataFrame(data)
#for tweets    
    else:
        extracted_data = pd.read_csv(args["file"])
        extracted_data = extracted_data[pd.notnull(extracted_data['text'])]
        extracted_data = extracted_data.reset_index(drop=True)
        extracted_data_new = []
        for i in range(0,len(extracted_data)):
            sent = extracted_data['text'][i]         
            extracted_data_new.append(" ".join(w for w in nltk.wordpunct_tokenize(sent) \
                                                     if w.lower() in words or not w.isalpha()))
        
        df_length = len(extracted_data_new)
        extracted_data_new = pd.DataFrame(np.array(extracted_data_new).reshape(df_length,1), columns = list("a"))
        extracted_data_new.columns=['text']                
        data = tm.get_data(query = extracted_data_new)
        fin_out = pd.DataFrame(data)

    
    for i in range(0,len(extracted_data_new)):
        try:
            #tweet = str(twitter_data['twt_text'][i])
            text = str(extracted_data_new['text'][i])
            text = text.replace(","," ")
            sentiment = str(fin_out['sentiment'][i])
            topic = str(fin_out['topics'][i])
            final_data = text+","+sentiment+","+topic
            print final_data.decode('ascii','ignore')
        
        except Exception ,e:
            pass
    
if __name__ == "__main__":
# calling main function
    main()