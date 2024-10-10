import json
from gensim.models import KeyedVectors

# Taken from here: https://code.google.com/archive/p/word2vec/
SOURCE_FILE = "./GoogleNews-vectors-negative300.bin"

# Word JSON file from here: https://github.com/dwyl/english-words/blob/master/words_dictionary.json
VALID_WORD_JSON_FILE = "./words_dictionary.json"


def load_word2vec():
    w2v = KeyedVectors.load_word2vec_format(SOURCE_FILE, binary=True)

    with open(VALID_WORD_JSON_FILE) as f:
        valid_words = json.load(f)
    keyset = valid_words.keys()
    return w2v.vectors_for_all(keyset)


def narrow_list(w2v, current_lst, current_word, current_similarity):
    sims = 1 - w2v.distances(current_word)
    small_lst = [
        k
        for k in range(sims.shape[0])
        if abs(sims[k] * 100 - current_similarity) <= 0.005
    ]
    return list(set(current_lst) & set(small_lst))


def main() -> None:
    w2v = load_word2vec()
    with open("./rasa.txt", "r") as f:
        rasa_sim_list = [float(x) for x in f.readlines()]
    with open("./abstainer.txt", "r") as f:
        abstainer_sim_list = [float(x) for x in f.readlines()]

    lst = list(range(len(w2v)))
    first_similarity = float(input("Enter similarity for 'tabula': "))
    lst = narrow_list(w2v, lst, "tabula", first_similarity)

    second_word = "uniaxial"
    for x in rasa_sim_list:
        # accounting for floating point shenanigans
        if abs(first_similarity - x) < 1e-6:
            second_word = "rasa"
    for x in abstainer_sim_list:
        # accounting for floating point shenanigans
        if abs(first_similarity - x) < 1e-6:
            second_word = "abstainer"
    second_similarity = float(input(f"Enter similarity for '{second_word}': "))
    lst = narrow_list(w2v, lst, second_word, second_similarity)

    if len(lst) == 0:
        print("No word found...")
        return

    assert len(lst) == 1

    print(f"Word found! Try '{w2v.index_to_key[lst[0]]}'")


if __name__ == "__main__":
    main()
