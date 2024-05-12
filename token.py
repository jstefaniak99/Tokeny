import re

def word_to_number(word):
    number_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10
    }
    return number_map.get(word.lower(), None)

def is_number(word):
    return word_to_number(word) is not None

def tokenize_text(text):
    tokens = []
    # Wykorzystanie biblioteki regex ułatwia prace ze zdaniami
    sentences = re.split(r'(?<=[.!?])\s+', text)  # podział tekstu na zdania
    for sentence_index, sentence in enumerate(sentences, start=1):
        words = re.findall(r'\b\w+\b', sentence)  # znalezienie wszystkich wystąpienia słów w tekście
        for word_index, word in enumerate(words, start=1):
            # Ustalenie typu słowa na podstawie ostatniego znalezionego zdania
            word_type = "word (Początek zdania)" if (sentence_index == 1 and word_index == 1) or (sentence_index > 1 and word_index == 1) else "word"
            number = word_to_number(word)
            if number is not None: # warunek do liczby
                word_type = "number"
                value = number 
            else:
                value = word.lower()
            token = f'Token ID: {word_index}\nWord: {word}\nType: {word_type}\nValue: {value}\n'
            tokens.append(token)
    return tokens

text = "Lorem ipsum dolor one amet, consectetur adipiscing elit. Nullam lacinia nec turpis vel auctor. Nam sed dui vehicula, tempus elit sed, hendrerit tellus."
tokens = tokenize_text(text)
for token in tokens:
    print(token)
