# # Task 1- Reverse a String

def reverse_string(word):
    reverse_word = " "

    for index in range(len(word)-1, -1, -1):
        reverse_word += word[index]
    return reverse_word

reversed_word = reverse_string("Hello")
print(reversed_word)

#  # Task 2- Capitalize a Letter

two_words = input()
print(two_words.title())

# Task 3: Palindrome
# - A “palindrome” is a word, phrase, or sequence that reads the same backward as
# forward i.e. madam
#     *Write code that takes a user input and checks to see if it is a Palindrome and
#     reports the result

word = input()
palindrome_word = word
for index in range(len(word) -1, -1, -1):
    palindrome_word == word[index]
    

print(palindrome_word)
print(" ")
    


 














