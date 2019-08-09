from collections import Counter
import operator

class Token2idx():
    def __init__(self):
        pass


    def build_from_tokens(self, tokens, most_freq_num=None):
        token_count = Counter(tokens)
        sorted_tokens = sorted(token_count.items(), key=operator.itemgetter(1), reverse=True)
        sorted_tokens = [a[0] for a in sorted_tokens]
        self.t2i = {article_id:idx+1 for idx, article_id in enumerate(sorted_tokens[:most_freq_num])}


    def load_token2idx(self, load_dir):
        with open(load_dir, 'r', encoding='utf-8') as f:
            self.t2i = json.load(f)


    def save_token2idx(self, save_dir):
        with open(save_dir, 'w', encoding='utf-8') as f:
            json.dump(self.t2i, f, ensure_ascii=False, indent=4)


    def token2idx(self, input):
        return list(map(lambda x: 0 if x is None else x, list(map(lambda x: self.t2i.get(x), input))))


    def get_token2idx(self):
        return self.t2i


    def get_idx2token(self):
        # WIP
        pass