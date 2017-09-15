#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections

import termextract.core
import termextract.japanese_plaintext

def output(data):
    f = open("jpn_plain_extracted.txt", "w", encoding="utf-8")
    data_collection = collections.Counter(data)
    for cmp_noun, value in data_collection.most_common():
        f.write(termextract.core.modify_agglutinative_lang(cmp_noun))
        f.write("\t")
        f.write(str(value))
        f.write("\n")
    f.close

if __name__ == "__main__":
    f = open("jpn_sample.txt", "r", encoding="utf-8")
    text = f.read()
    f.close
    frequency = termextract.japanese_plaintext.cmp_noun_dict(text)
    # term_list = termextract.japanese_plaintext.cmp_noun_list(text)
    LR = termextract.core.score_lr(frequency, lr_mode=1, average_rate=1)
    term_imp = termextract.core.term_importance(frequency, LR)
    output(term_imp)
