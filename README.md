# Semantle Solver
Corresponds to my blog post "Writing a Semantle Solver" on [https://asjchen.github.io/](https://asjchen.github.io/).

1. In your favorite virtual environment setup, install `gensim`, say with:
```
pip install gensim==4.3.3
```
2. Download the pretrained word2vec file `GoogleNews-vectors-negative300.bin` [here](https://code.google.com/archive/p/word2vec/). It's under the "Pre-trained word and phrase vectors" section.
3. Download the `words_dictionary.json` file from [here](https://github.com/dwyl/english-words/blob/master/words_dictionary.json).
4. Run `python three_guess_strategy.py`, which will prompt stdin input with your observed similarities.
