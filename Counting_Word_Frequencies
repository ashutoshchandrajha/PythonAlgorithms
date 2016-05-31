freq = {}
for piece in open("C:\Ashutosh Jha\Study Materials\\frequent_word_example.txt").read().lower().split():
    # only consider alphabetic character within this piece
    word = ''.join(c for c in piece if c.isalpha())
    if word:                        #requires atleast one alphabetic character
        freq[word] = 1 + freq.get(word, 0)

max_word = ''
max_count = 0
for (w,c) in freq.items():      # (key, value) tuples represent (word, count)
    if c > max_count:
        max_word = w
        max_count = c

print ('The most frequent word is =',max_word)
print ('Its number of occurences is =', max_count)

"""OUTPUT
The most frequent word is = the
Its number of occurences is = 21
"""
