# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 19:38:59 2018

@author: Jennifer
"""
#txt file import
import os
import glob
from unidecode import unidecode
import codecs
#data manipulation
import pandas as pd 
import numpy as np
#word manipulation
from nltk.tokenize import word_tokenize     


corpus_root = 'C:\\Users\\Jennifer\\Documents\\Berkeley\\W266\\Final Project\\Final-dataset\\bins' 

txtfiles = [os.path.join(root, name)
             for root, dirs, files in os.walk(corpus_root)
             for name in files
             if name.endswith(".txt")]

books = []
tags = []
#for root, dirs, files in os.walk(corpus_root):
#    for name in files
    #for name in files:
for path in txtfiles:
    #for filename in (path):
    #for filename in (path):
    #if path.endswith('.txt'):
    #with codecs.open(path,'r',encoding="utf-8", errors='ignore').read() as df_book:
    df_book = open(path,'r').read()
    #print(df_book)
    df_book = df_book.decode('ascii', 'replace') #'utf-8',)\
    #df_book = df_book.encode('utf-8',)
    books.append(df_book)
    test= (str(path)[75:])
    tags.append(test)

books_test = pd.DataFrame(books)        
books_test['tags'] = tags
books_test['bookID'], books_test['sectionID'] = books_test['tags'].str.split('\\').str
books_test['sectionID'] = books_test['sectionID'].str.replace('\.txt', '')

#books_test[0] = books_test[0].apply(unidecode)
#books_test[0] = books_test[0].apply(lambda x: pd(unidecode(x)))
#final_dataset[1] = final_dataset[1].apply(unidecode)


books_test.to_csv("midpoint_context.csv", sep='\t', encoding='utf-8')


###########################################
#CODE GRAVEYARD
#df_book1 = pd.DataFrame(df_book3)

#from nltk.corpus import PlaintextCorpusReader
#import nltk

#corpus = nltk.corpus.reader.plaintext.PlaintextCorpusReader
#corpus_root = 'C:/Users/Jennifer/Documents/Berkeley/W266/Final Project/Final-dataset/Bins' 
#wordlists = PlaintextCorpusReader(corpus_root, '.*txt') 
#wordlists.fileids()d = dict()
#df_book_str = pd.DataFrame()
#d[1] = ({"bookID": "1" ,"Content": df_bookB})
#d[2] = ({"bookID": "2", "Content": df_book3})

#tokens2 = word_tokenize(df_bookB)
#tokens2 = [w.lower() for w in tokens2]          
#tokens2 = np.asarray (tokens2)           
#       #   pd.DataFrame({'A': [0, 4, 5, 6, 7, 7, 6,5]})
#df_books = [tokens,tokens2]
#df_books = pd.DataFrame(df_books)
#
#tokens = word_tokenize(df_book3)
#tokens = [w.lower() for w in tokens]
#tokens = np.asarray (tokens)   

#df_bookA  = open('05.txt','r')
#df_bookB = df_bookA.read()
#print(message)
#df_bookA.close()


#df_books = tokens + tokens2
#df_books.append(tokens)          
#books = pd.DataFrame(d.items(), columns=['bookID', 'Content'])
#books.append(df_book3)

#wordlists = PlaintextCorpusReader(corpus_root, '.*')
#df_book1 = pd.read_csv('04.txt', error_bad_lines=False)


#df_book  = glob.glob(filename,'r').read()
#print(message)
#df_book2.close()
##page = urllib.urlopen(filename).read()

#books_test['tags'].str.split('\\', 1, expand =True)
#books_test['sectionID'] = str(path)[75:]
#books_test.index +1


#referenced : https://machinelearningmastery.com/clean-text-machine-learning-python/