from books import Good_Reads_All_Time
from books import Good_Reads_Young_Adult
from words import English_10000

titles = Good_Reads_All_Time + Good_Reads_Young_Adult

for title in titles:
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
