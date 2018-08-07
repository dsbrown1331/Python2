import sys
sys.path.append("/home/dsbrown/Documents/ACES/github/Python2/")
from Dictionaries import text_summarization as ts

filename = "../Data/alice_in_wonderland.txt"
stopwords = "../Data/stop_words.txt"
word_cnts = ts.count_word_freqs(filename, stopwords)
print(word_cnts)
print('the', word_cnts.get('the',0))
print('alice', word_cnts.get('alice',0))
print('liberty', word_cnts.get('liberty',0))
print("most common word", ts.most_freq_word(word_cnts))
