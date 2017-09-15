#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections

import termextract.english_plaintext
import termextract.core

def output(data):
    f = open("eng_plain_extracted.txt", "w", encoding="utf-8")
    data_collection = collections.Counter(data)
    for cmp_noun, value in data_collection.most_common():
        f.write(cmp_noun)
        f.write("\t")
        f.write(str(value))
        f.write("\n")
    f.close

if __name__ == "__main__":
    f = open("eng_sample.txt", "r", encoding="utf-8")
    text = f.read()
    f.close
    frequency = termextract.english_plaintext.cmp_noun_dict(text)
    # term_list = termextract.english_plaintext.cmp_noun_list(text)
    LR = termextract.core.score_lr(frequency,
             ignore_words=termextract.english_plaintext.IGNORE_WORDS,
             lr_mode=1, average_rate=1
         )
    term_imp = termextract.core.term_importance(frequency, LR)
    output(term_imp)
