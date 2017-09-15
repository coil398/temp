#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections
import dbm

import termextract.mecab
import termextract.core

def output(data):
    f = open("mecab_extracted.txt", "w", encoding="utf-8")
    data_collection = collections.Counter(data)
    for cmp_noun, value in data_collection.most_common():
        f.write(termextract.core.modify_agglutinative_lang(cmp_noun))
        f.write("\t")
        f.write(str(value))
        f.write("\n")
    f.close

if __name__ == "__main__":
    f = open("mecab_out_sample.txt", "r", encoding="utf-8")
    tagged_text = f.read()
    f.close

    frequency = termextract.mecab.cmp_noun_dict(tagged_text)
    #term_list = termextract.mecab.cmp_noun_list(tagged_text)
    LR = termextract.core.score_lr(frequency,
             ignore_words=termextract.mecab.IGNORE_WORDS,
             lr_mode=1, average_rate=1
         )
    term_imp = termextract.core.term_importance(frequency, LR)
    output(term_imp)
