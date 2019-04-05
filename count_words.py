from janome.tokenizer import Tokenizer
import json
from collections import Counter, defaultdict
from get_tweets import get_tweets


def count_words(texts):
    tokenizer = Tokenizer()

    # 原形に変形、名詞のみ、1文字を除去
    collection = Counter(token.base_form for token in tokenizer.tokenize(texts)
                         if token.part_of_speech.startswith('名詞') and len(token.base_form) > 1)

    freq_dict = {}

    most_common = collection.most_common()

    for mc in most_common:
        freq_dict[mc[0]] = mc[1]
    fw = open('word_rank.json', 'w')
    json.dump(freq_dict, fw, indent=4)
    return freq_dict


if __name__ == '__main__':
    count_words(get_tweets('靖国神社', '201312260800', '201312261000'))
    