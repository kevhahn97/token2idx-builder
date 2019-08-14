# Token2idx-builder
## Description
This module builds an token2idx vocab dictionary for given list of tokens. (Tokenized corpus)

## Usage
### 1. Import
```
from token2idx import Token2idx
t2i = Token2idx()
```
### 2. Tokenize corpus
```
corpus = "반갑습니다. 제 이름은 한승호입니다. 제 취미는 자연어처리입니다."
tokens = corpus.split()
```
### 3. Build
```
t2i.build_from_tokens(tokens, most_freq_num=4)
```
You can use most_freq_num option to build a vocab only with certain number of most frequently used words.
### 4. Use
```
print(t2i.token2idx(tokens))
```
id 0 is for OOV

## To do
### 1. Idx2token
