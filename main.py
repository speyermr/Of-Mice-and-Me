from books import Good_Reads
from words import English_10000

for title in Good_Reads:
  words = title.split(' ')
  last_word = words[-1]
  last_word_truncated = last_word[0:-1].lower()

  if False:
    continue

  if last_word_truncated in English_10000:
    new_words = words[0:-1]
    new_words.append(last_word_truncated.capitalize())
    new_title = ' '.join(new_words)
    print(title, '->', new_title)