#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections
import dbm

import termextract.mecab
import termextract.core

def output(data):
    f = open("mecab_extracted-store_lr.txt", "w", encoding="utf-8")
    data_collection = collections.Counter(data)
    for cmp_noun, value in data_collection.most_common():
        f.write(termextract.core.modify_agglutinative_lang(cmp_noun))
        f.write("\t")
        f.write(str(value))
        f.write("\n")
    f.close

if __name__ == "__main__":
    # LRの情報を蓄積（事前処理）
    db = dbm.open("termextrat", "n")
    input_files = ["mecab_out_sample.txt", "mecab_out_sample2.txt", "mecab_out_sample3.txt"]
    for file in input_files:
        f = open(file, "r", encoding="utf-8")
        tagged_text = f.read()
        f.close
        frequency = termextract.mecab.cmp_noun_dict(tagged_text)
        termextract.core.store_lr(frequency, dbm=db)
    db.close

    # 専門用語抽出対象の文書を読み込み
    f = open("mecab_out_sample.txt", "r", encoding="utf-8")
    tagged_text = f.read()
    f.close
    frequency = termextract.mecab.cmp_noun_dict(tagged_text)

    # 蓄積したLR情報からLRを呼び出し
    db = dbm.open("termextract", "r")
    LR = termextract.core.score_lr(frequency,
             ignore_words=termextract.mecab.IGNORE_WORDS,
             lr_mode=1, average_rate=1, dbm=db
         )
    db.close
 
    # 重要度をfrequencyとLRの組み合わせとし、ファイル出力
    term_imp = termextract.core.term_importance(frequency, LR)
    output(term_imp)
