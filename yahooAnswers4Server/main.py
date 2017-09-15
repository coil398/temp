import crawler
from textsPreprocessor import TextsPreprocessor
import sys
import os
from use_termext import use_termext


def main(keyword, times):
    YACrawler = crawler.Processor4YA()
    questions, answers = YACrawler.crawl(keyword, times)
    preprocessor = TextsPreprocessor(keyword)
    questions = preprocessor.preprocess(questions)
    answers = preprocessor.preprocess(answers)
    dir_path = 'result/' + keyword
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    question_path = dir_path + '/questions.txt'
    answer_path = dir_path + '/answers.txt'
    question_output_path = dir_path + '/questions_output.txt'
    answer_output_path = dir_path + '/answers_output.txt'
    paths = [question_path, answer_path, question_output_path, answer_output_path]
    if os.path.exists(paths[0]):
        os.remove(paths[0])
    if os.path.exists(paths[1]):
        os.remove(paths[1])
    if os.path.exists(paths[2]):
        os.remove(paths[2])
    if os.path.exists(paths[3]):
        os.remove(paths[3])
    with open(paths[0], 'a') as f:
        f.write(questions)
    with open(paths[1], 'a') as f:
        f.write(answers)
    use_termext(paths)


if __name__ == '__main__':
    keyword = sys.argv[1]
    # times = int(sys.argv[2])
    main(keyword, times=3)
