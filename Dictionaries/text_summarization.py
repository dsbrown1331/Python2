import string


def get_stop_words(filename):
    stops = []
    reader = open(filename)
    for word in reader:
        stops.append(word.strip())
    return stops

#reads a file and counts word frequencies
#in a dictionary
#return dictionary of word frequencies
def count_word_freqs(filename, ignorefile = None):

    if ignorefile is None:
        ignore_list = []
    else:
        ignore_list = get_stop_words(ignorefile)
    d = dict()
    reader = open(filename)
    for line in reader:
        #delete all punctuation in the line
        l = line.translate(line.maketrans('', '', string.punctuation))
        #separate out words, make all lowercase
        for word in l.lower().split():
            if word not in ignore_list:
                d[word] = d.get(word, 0) + 1

    return d


#returns most frequent key and corresponding value
def most_freq_word(freq_dict):
    max_freq = 0
    max_freq_word = ""
    for word in freq_dict:
        #get frequency of word
        freq = freq_dict[word]
        if freq > max_freq:
            max_freq = freq
            max_freq_word = word
    return max_freq_word, max_freq


if __name__ == "__main__":
    filename = "../Data/alice_in_wonderland.txt"
    stopwords = "../Data/stop_words.txt"
    word_cnts = count_word_freqs(filename, stopwords)
    print(word_cnts)
    print('the', word_cnts.get('the',0))
    print('alice', word_cnts.get('alice',0))
    print('liberty', word_cnts.get('liberty',0))
    print("most common word", most_freq_word(word_cnts))
    #TODO: call count_word_freqs and print the result
    #TODO: print out the most common word in the file
