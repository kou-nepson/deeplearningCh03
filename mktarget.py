import sys
sys.path.append('..')
from preprocess import preprocess, create_contexts_target, convert_one_hot

text = 'You say goodbye and I say hello.'
corpus, word_to_id, id_to_word = preprocess(text)
print(corpus)

print(id_to_word)

contexts, target = create_contexts_target(corpus, window_size=1)

print(context)

print(target)
