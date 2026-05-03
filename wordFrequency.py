def word_frequency(sentence = "hello world hello"):
    words = sentence.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word,0) + 1
    print(counts)

word_frequency()