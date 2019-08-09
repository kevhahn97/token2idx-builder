from token2idx import Token2idx
t2i = Token2idx()

# tokenize corpus
corpus = "반갑습니다. 제 이름은 한승호입니다. 제 취미는 자연어처리입니다."
tokens = corpus.split()
print(tokens)
# ['반갑습니다.', '제', '이름은', '한승호입니다.', '제', '취미는', '자연어처리입니다.']

# build token2idx
t2i.build_from_tokens(tokens, most_freq_num=4)
print(t2i.get_token2idx())
# {'제': 1, '반갑습니다.': 2, '이름은': 3, '한승호입니다.': 4}

# usage
print(t2i.token2idx(tokens))
# [2, 1, 3, 4, 1, 0, 0]