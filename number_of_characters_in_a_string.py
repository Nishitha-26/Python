#  Excludes spaces using a loop
def number_of_chars(s):
    """
    Counts number of characters in a string excluding spaces.
    :param s: str: Takes input as a string.
    :return: int: Returns the count of characters.
    """
    count = 0
    for i in s:
        if i != " ":
            count += 1
    return count


s = "Python is a popular programming language"
print(number_of_chars(s))


# Excludes spaces using replace() and len()

def number_of_characters(s):
    """
     Counts number of characters in a string excluding spaces.
    :param s: str: Takes input as a string.
    :return: int: Returns the count of characters.
    """
    a = s.replace(" ", "")
    return len(a)


s = "Python is a popular programming language"
print(number_of_characters(s))


#  Includes spaces using a loop

def number_of_characters(s):
    """
    Counts number of characters in a given string including spaces.
    :param s: str: Takes input as a string.
    :return: int : Returns the count of  each character.
    """
    count = 0
    for i in s:
        count += 1
    return count


s = "Python is a popular programming language"
print(number_of_characters(s))


#  Includes spaces using len()

def number_of_characters(s):
    """
    Counts number of characters in a given string including spaces.
    :param s: str: Takes input as a string.
    :return: int : Returns the count of  each character.
    """
    return len(s)


s = "Python is a popular programming language"
print(number_of_characters(s))