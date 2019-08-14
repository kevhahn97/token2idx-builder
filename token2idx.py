from collections import Counter
import operator

class Token2idx():
    def __init__(self):
        pass

    def build_from_tokens(self, tokens, most_freq_num=None):
        token_count = Counter(tokens)
        sorted_tokens = sorted(token_count.items(), key=operator.itemgetter(1), reverse=True)
        sorted_tokens = sorted_tokens[:most_freq_num]
        self.coverage = sum([a[1] for a in sorted_tokens]) / len(tokens)
        sorted_tokens = [a[0] for a in sorted_tokens]
        self.t2i = {article_id:idx+1 for idx, article_id in enumerate(sorted_tokens)}
        print('vocab coverage:', self.coverage)
        if most_freq_num is None:
            self.vocab_size = len(sorted_tokens)
        else:
            self.vocab_size = most_freq_num
        print('with vocab size:', self.vocab_size)


    def load_token2idx(self, load_dir):
        with open(load_dir, 'r', encoding='utf-8') as f:
            self.t2i = json.load(f)


    def save_token2idx(self, save_dir):
        with open(save_dir, 'w', encoding='utf-8') as f:
            json.dump(self.t2i, f, ensure_ascii=False, indent=4)


    def token2idx(self, input):
        return list(map(lambda x: self.t2i.get(x, 0), input))


    def get_token2idx(self):
        return self.t2i


    def get_idx2token(self):
        # WIP
        pass