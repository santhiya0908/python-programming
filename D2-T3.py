def max_words_in_sentence(sentences):
    max_words = 0
    for sentence in sentences:
        num_words = len(sentence.split())
        max_words = max(max_words, num_words)
    return max_words

sentences = ["This is a sentence.", "This is another sentence.", "This is a longer sentence with more words."]
print("Maximum number of words:", max_words_in_sentence(sentences))
