# This script replaces the first occurrence of a specified word in a sentence with a new word.
# Enter a sentence, the word you want to replace, and the replacement word when prompted.
# The script will replace the first occurrence of the word and display the updated sentence.

sentence = input("Enter a sentence: ")
wordtoreplace = input("Enter word to replace: ")
replacement = input("Enter replacement word: ")

newsen = sentence.replace(wordtoreplace, replacement, 1)

print(newsen)
