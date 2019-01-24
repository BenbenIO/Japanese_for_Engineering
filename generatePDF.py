# -*- coding: utf-8 -*-
# Japanese for Engineer
# Generate PDF file from csv
# Calling method: python generatePDF --topic --mode
# mode: 0: noblank - 1: Kanji test - 2: reading test - 3: translation test - 4: random test 
# Advice for printing the pdf: Mutliple page: 2 by 1 / Landscape / both sides of paper

import pandas as pd
import numpy as np
import random
from pdf_reports import pug_to_html, write_report
import os
import sys
from time import gmtime, strftime

# Global variable
pdf_path = "PDF/"

# Blank generation
def noblank(vocabulary):
    modetile = "no_blank"
    return vocabulary,modetile

def kanjitest(vocabulary):
    findkanji = vocabulary.copy()
    findkanji.kanji = " "
    modetitle = "kanji_blank"
    return findkanji, modetitle

def hiraganatest(vocabulary):
    findhiragana = vocabulary.copy()
    findhiragana.hiragana = " "
    modetitle = "hiragana_blank"
    return findhiragana, modetitle

def englishtest(vocabulary):
    findenglish = vocabulary.copy()
    findenglish.english = " "
    modetitle = "english_blank"
    return findenglish, modetitle

def randomtest(vocabulary):
    listlen = vocabulary.shape[0]

    replacevector = []
    for i in range(listlen):
        replacevector.append(random.randint(0,2))

    findrandom = vocabulary.copy()
    for i in range(listlen):
        findrandom.iloc[i,replacevector[i]] = " "
    modetitle = "random_blank"
    return findrandom, modetitle

def main():
    # Get user input
    topic = sys.argv[1]
    mode = int(sys.argv[2])
    
    # Mode dictionary 
    modeselect = {
        0: noblank,
        1: kanjitest,
        2: hiraganatest,
        3: englishtest,
        4: randomtest,
    }
    
    # import vocabulary from csv file
    filename = topic + ".xls"
    try:
        vocabulary = pd.read_excel("xls_files/" + filename)
        vocabulary.columns = ['kanji', 'hiragana', 'english']
    except:
        print("Filename "+"xls_files/" + filename+" invalid (wrong path or xls format invisible character)")
        return(1)
    
    try:
        toprint, modetitle = modeselect.get(mode, lambda: "error mode")(vocabulary)
        # Shuffle
        toprint = toprint.iloc[np.random.permutation(len(toprint))]
    except:
        print("Mode "+ str(mode) +" invalid")
        print("Mode => 0: noblank - 1: Kanji test - 2: reading test - 3: translation test - 4: random test")
        return(1)
        
    # Convert to pdf
    date = strftime("%Y_%m_%d", gmtime())
    pdffilename = topic + "_" + modetitle + "_" + date
    html = pug_to_html("template.pug", title="Japanese for Engineering",
                       vocab = topic, dataframe=toprint,
                       size = len(toprint))
    
    try:
        print("PDF saving as " + pdffilename )
        write_report(html, pdf_path + pdffilename +".pdf")
        print("Done !")
        return(0)
    except:
        print("Please close the existing pdf with the same name")
        return(1)
        
if __name__ == '__main__':
    main()