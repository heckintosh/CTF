def insert_hair_spaces(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Join the words with 10 Hair Spaces in between
    spaced_sentence = '\u200A' * 10
    spaced_sentence = spaced_sentence.join(words)

    return spaced_sentence

# Example usage:
input_sentence = "thing real person  down  fact part way at set program people plan other open only of move while  through get"
result = insert_hair_spaces(input_sentence)

print(result)
