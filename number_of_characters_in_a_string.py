def number_of_chars(string):
    """
    Counting number of characters in a string excluding space
    :param string: str: Takes input as a string
    :return: int: Returns the count of characters
    """
    count = 0
    for i in string:
        if i != " ":
            count += 1
    return count

string = "Python is a popular programming language"
print(number_of_chars(string))

