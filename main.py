from books import Good_Reads
from words import English_10000

#
# Example
#
title = 'The Hunger Games'

words = title.split(' ')        # split!
print(words)

# The first word (index=0)
print(words[0])

# The third word (index=2)
print(words[2])

# The last word (index=-1 ... one in from the end)
last_word = words[-1]
print(last_word)

# The first character of the last word
print(last_word[0])

# The last character of the last word
print(last_word[-1])

# Everything up to (but not including) the last character
print(last_word[0:-1])


for book_title in Good_Reads:
    book_words = book_title.split(' ')
    last_word = book_words[-1]
    last_word_truncated = last_word[0:-1].lower()
    if last_word_truncated in English_10000:
        #print(book_title)
        #print(book_title[0:-1])
        pass
