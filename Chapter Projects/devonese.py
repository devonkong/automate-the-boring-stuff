# English to Devonese translator.

message = input("Enter the English message to translate into Devonese:")

vowels = ('a', 'e', 'i', 'o', 'u', 'y')

devonese = []  # A list of words in Devonese.

for word in message.split():
    # Separate the non-letters at the start of this word:
    prefix_non_letters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefix_non_letters += word[0]
        word = word[1:]
    if len(word) == 0:
        devonese.append(prefix_non_letters)
        continue
    
    # Separate the non-letters at the end of this word:
    suffix_non_letters = ''
    while len(word) != 0 and not word[-1].isalpha():
        suffix_non_letters += word[-1]
        word = word[:-1]
        
    # Remember if the word was in uppercase or title case, of if it was the contraction "I'm".
    was_upper = word.isupper()
    was_title = word.istitle()
    was_contraction = word.lower() == "i'm"
    
    word = word.lower()  # Make the word lowercase for translation.
    
    # Separate the consonants at the start of this word:
    prefix_consonants = ''
    while len(word) > 0 and not word[0] in vowels:
        prefix_consonants += word[0]
        word = word[1:]
        
    # Add Devonese ending to the word:
    if prefix_consonants != '':
        word += prefix_consonants + 'in'
    else:
        word += 'vin'
    
    # Set the word back to uppercase or title case:
    if was_upper:
        word = word.upper()
    if was_title:
        word = word.title()
    if was_contraction:
        word = word.capitalize()  # Capitalize the "I'm" contraction
        
    # Add the non-letters back to the start or end of the word.
    devonese.append(prefix_non_letters + word + suffix_non_letters)
    
# Join all the words back together into a single string:
print(' '.join(devonese))