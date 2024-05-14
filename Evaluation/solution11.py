words=["ca", "dog", "sun", "cup", "communication"]
long_word="comunication"

for word in words:
    if len(words) > len(long_word):
        long_word=word

print(long_word)