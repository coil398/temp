#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections
import dbm

import termextract.mecab
import termextract.core

def output(data):
    f = open("mecab_extracted-tfidf.txt", "w", encoding="utf-8")
    data_collection = collections.Counter(data)
    for cmp_noun, value in data_collection.most_common():
        f.write(termextract.core.modify_agglutinative_lang(cmp_noun))
        f.write("\t")
        f.write(str(value))
        f.write("\n")
    f.close

if __name__ == "__main__":
    # DF情報を蓄積
    input_files = ["mecab_out_sample.txt", "mecab_out_sample2.txt", "mecab_out_sample3.txt"]
    df = dbm.open("df", "n")
    for file in input_files:
        f = open(file, "r", encoding="utf-8")
        tagged_text = f.read()
        f.close
        frequency = termextract.mecab.cmp_noun_dict(tagged_text)
        termextract.core.store_df(frequency, dbm=df)
    df.close


    # 処理対象のテキスト（事前にDFに読み込ませる必要あり）を呼び出し
    f = open("mecab_out_sample.txt", "r", encoding="utf-8")
    tagged_text = f.read()
    f.close
    frequency = termextract.mecab.cmp_noun_dict(tagged_text)

    # FerequencyからTFを生成する
    TF = termextract.core.frequency2tf(frequency)

    # 蓄積したDF情報からIDFを呼び出し。
    df = dbm.open("df", "r")
    IDF = termextract.core.get_idf(frequency, dbm=df)
    df.close
 

    # 重要度をTFとIDFの組み合わせとし、ファイル出力
    term_imp = termextract.core.term_importance(TF, IDF)
    output(term_imp)
