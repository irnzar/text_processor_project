import text_processor as tp

textstr = input("Please enter a text: ")

print(f"Text wo punctuation: {tp.remove_punctuation(textstr)}")

print (f"Text to lowercase: {tp.convert_to_lowercase(textstr)}")

print (f"Text to words: {tp.tokenize_text(textstr)}")

print (f"Sentence tokenize: {tp.sentence_tokenize(textstr)}")

print (f"Word count: {tp.word_count(textstr)}")

print (f"Character count: {tp.character_count(textstr)}")


