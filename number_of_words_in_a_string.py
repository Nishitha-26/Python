#  Counts words using split() and a loop
def number_of_words(s):
    """
    Counting number of words in a string
    :param s: str: Takes input as a string
    :return: int: Returns the count of words
    """
    words = s.split()
    count = 0
    for i in words:
        count += 1
    return count

s = "Python is a popular programming language"
print(number_of_words(s))

#   Counts words manually using character-by-character
def number_of_words(s):
    """
    Counting number of words in a string
    :param s: str: Takes input as a string
    :return:  int: Returns the count of words
    """
    temp = ""
    words = []
    count = 0
    for i in s:
        if i != " ":
            temp += i
        else:
            if temp:
                words.append(temp)
                temp = ""
                count += 1
    if temp:
        words.append(temp)
    count += 1
    return count
s = "Python is a popular programming language"
print(number_of_words(s))

# Counts words using len()and split()
def number_of_words(s):
    """
    Counting number of words in a string
    :param s:  str: Takes input as a string
    :return: int: Returns the count of words
    """
    return len(s.split())
s = "Python is a popular programming language"
print(number_of_words(s))





