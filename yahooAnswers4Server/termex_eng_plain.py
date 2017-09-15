#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections
import dbm

import termextract.english_plaintext
import termextract.core


def output(data, outputFile):
    f = open(outputFile, "a", encoding="utf-8")
    data_collection = collections.Counter(data)
    for cmp_noun, value in data_collection.most_common():
        f.write(cmp_noun)
        f.write("\t")
        f.write(str(value))
        f.write("\n")
    f.close


def main(inputFile, outputFile):
    f = open(inputFile, "r", encoding="utf-8")
    text = f.read()
    f.close
    frequency = termextract.english_plaintext.cmp_noun_dict(text)
    # term_list = termextract.english_plaintext.cmp_noun_list(text)
    db = dbm.open('termextract', 'c')
    LR = termextract.core.score_lr(frequency,
                                   ignore_words=termextract.english_plaintext.IGNORE_WORDS,
                                   lr_mode=1, average_rate=1,
                                   dbm=db)
    term_imp = termextract.core.term_importance(frequency, LR)
    output(term_imp, outputFile)
