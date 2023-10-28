# sentence = input("Enter a sentence: ")
# word = input("Enter a word: ")

# # Check if the word matches any part of the sentence
# if word in sentence:
#     index = sentence.index(word)
#     print(index)
# else:
#     print("no match")

# Input sentence and word
chosen = input("Enter a sentence: ")
chosen_word = input("Enter a word: ")

# Check if the word matches any part of the sentence as a whole word
if f" {chosen_word} " in f" {chosen} ":
    index = chosen.index(chosen_word)
    print(index)
else:
    print("no match")

