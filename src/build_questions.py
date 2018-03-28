# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 13:56:14 2018

@author: Jennifer
"""

import urllib
#import HTMLParser
from bs4 import BeautifulSoup
import re
import numpy as np
import pandas as pd
import os
from unidecode import unidecode
#import cssutils

final_dataset = pd.DataFrame()
#print(parsed_html)
bookIDs = [79, 35, 83,85, 86,87,88, 90,91,92,94,95,96,98,100,101,102,103,105,106, 109,110,12,108, 89,77]
for book in (bookIDs):
    #book = 89
    filename = str(book) + '.htm'
    page = urllib.urlopen(filename).read()
    #print (page)
    parsed_html = BeautifulSoup(page)
    questions = []
    answers = []
    for section in parsed_html.findAll('span', attrs={'style':'font-size:24.0pt;color:black'}):
            print section.next
            #for spellcheck in parsed_html.findAll('span',{'class':'SpellE'}):
            #    spellcheck.replaceWith('')    
            for question in parsed_html.findAll('span', attrs={'style':'font-size:12.0pt;color:black'}):
                #print 
                #questions.append(question.next)
                answers.append(question.text)
                #print( "BREAK")
    
    df = np.asarray(answers)
    just_questions = df # [0:348]
    just_questions = np.reshape(just_questions,((len(df)/2),2))
    just_questions = pd.DataFrame(just_questions)
    just_questions[2]= book
    final_dataset = pd.concat([just_questions, final_dataset])
    #final_dataset.append(just_questions)
    #.decode("utf-8", "ignore") 
    final_dataset[question] = final_dataset[question].apply(unidecode)
final_dataset.to_csv("midpoint_questions.csv", sep='\t') #,encoding='utf-8')
