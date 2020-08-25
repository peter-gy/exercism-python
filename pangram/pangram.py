import string

alphabet_list = list(string.ascii_lowercase)

def is_pangram(sentence):
    character_list = list(sentence.lower())
    return all(character in character_list for character in alphabet_list)