#  Using split() and a loop to process each word
def number_of_chars(word):
    """
    Counts the number of characters in a given word.
    :param word: str - A word from string.
    :return: int - Number of characters in each word.
    """
    count = 0
    for i in word:
        count += 1
    return count
string = "python is a popular programming language"
words = string.split()
for word in words:
    print(f"{word}:{number_of_chars(word)}")

# Manual word separation using character-by-character logic
def number_of_chars(word):
    """
    Counts the number of characters in a given word.
    :param word: str - A word from string.
    :return: int - Number of characters in each word.
    """
    count = 0
    for i in word:
        count += 1
    return count

string = "python is a popular programming language"
current_word = ""
for char in string:
    if char != " ":
        current_word += char
    else:
        if current_word != "":
            print(f"{current_word}: {number_of_chars(current_word)}")
            current_word = ""

if current_word != "":
    print(f"{current_word}: {number_of_chars(current_word)}")

# By using len() and split()
def number_of_chars(word):
    """
    Counts the number of characters in a given word.
    :param word: str - A word from string.
    :return: int - Number of characters in each word.
    """
    return len(word)
string = "python is a popular programming language"
words = string.split()
for word in words:
    print(f"{word}:{number_of_chars(word)}")
