#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections

import pynlpir
import termextract.nlpir
import termextract.core

def output(data):
    f = open("nlpir_extracted.txt", "w", encoding="utf-8")
    data_collection = collections.Counter(data)
    for cmp_noun, value in data_collection.most_common():
        f.write(termextract.core.modify_agglutinative_lang(cmp_noun))
        f.write("\t")
        f.write(str(value))
        f.write("\n")
    f.close

if __name__ == "__main__":
    f = open("chi_sample.txt", "r", encoding="utf-8")
    text = f.read()
    f.close
    pynlpir.open()
    text = text.replace('\n',' ') # 改行は削除しておく
    tagged_text = pynlpir.segment(text)
    frequency = termextract.nlpir.cmp_noun_dict(tagged_text)
    # term_list = termextract.nlpir.cmp_noun_list(tagged_text)
    LR = termextract.core.score_lr(frequency,
             ignore_words=termextract.nlpir.IGNORE_WORDS,
             lr_mode=1, average_rate=1
         )
    term_imp = termextract.core.term_importance(frequency, LR)
    output(term_imp)
