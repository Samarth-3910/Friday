def is_rhyme(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()

    vowels = 'aeiou'

    # Find the last vowel in word1
    last_vowel_index_1 = next((i for i in range(len(word1) - 1, -1, -1) if word1[i] in vowels), -1)

    # Find the last vowel in word2
    last_vowel_index_2 = next((i for i in range(len(word2) - 1, -1, -1) if word2[i] in vowels), -1)

    # Compare the ending sounds
    return word1[last_vowel_index_1:] == word2[last_vowel_index_2:]

# Example usage
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
if is_rhyme(word1, word2):
    print("The words rhyme!")
else:
    print("The words don't rhyme.")
