# This script replaces a specific word in a sentence with a new word provided by the user.
# The user is prompted to enter a sentence, the word to replace, and the replacement word.
# The script replaces the specified word in the sentence and prints the updated sentence.

sentence = input("Enter a sentence:")
word = input("Enter the word to replace: ")
replaceWord =input("Enter replacement word: ")

sentence = sentence.replace(word, replaceWord)
print(sentence)
