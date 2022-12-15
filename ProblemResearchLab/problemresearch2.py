# # # Task 1- Reverse a String

# def reverse_string(word):
#     reverse_word = word

#     for index in range(len(word)-1, -1, -1):
#         reverse_word += word[index]
   

# reversed_word = reverse_string("Hello")
# print(reversed_word)

# #  # Task 2- Capitalize a Letter
# Write code that takes a string as input and capitalize the first letter of each word. 
# Words will be separated by only one space. i.e. “hello world” should be outputted as “Hello World”


# How do I capitalize the first letter of a word?
# - how do we access the first index of a word? word[0]
# - how do I capitalize a single letter? word[0].upper() - .upper() is parameterless

def capitalizer(word):
    # insead of looping over each char, loop over each index in the word
    # how do I produce a list of numbers, representing the indexes in the word ([0, 1, 2, 3, 4]) for loop w range fn
    # I want the range to start at 0, and end (2nd argument) at ?
    for index in range(0, len(word)):
      #word = word[0].upper() + word[1:]
        word = (word[0].upper()+word[1:])
        
        
    
        

        
        
        

capitalizer("hello")


def titleizer(sentence):
    pass

titleizer("hello world")





# # Task 3: Palindrome
# # - A “palindrome” is a word, phrase, or sequence that reads the same backward as
# # forward i.e. madam
# #     *Write code that takes a user input and checks to see if it is a Palindrome and
# #     reports the result

# word = input("")
# reverse_word = word

# if reverse_word >= reverse_string:
#     print(reverse_word)
# else:
#     print("Sorry not a palindrome word.")

    

# print(palindrome_word)
# print(" ")

# Task 4 : Compress a string of characters
    
# comp_string = "aaacccgghhhbbssssddd"
# print(comp_string)


 














