
def wordcount(text):
     #this function counts the words in a sentence or a paragraph 
    words = text.split()
    return len(words)

#  Prompt the user to enter a sentence or paragraph
user_input = input("Enter a sentence or paragraph: ")

# checking error for empty input
if not user_input.strip():
        print("Error: empty string, run again")
else:
        word_count = wordcount(user_input)
        # Display the word count to the user
        print("number of words in your sentence or paragraph :", word_count)


