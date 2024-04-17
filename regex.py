"""
Regular Expressions and Text Normalization in Python

File Name: lab_2.py
Author: Ken Howry
Date: 5.4.24
Course: COMP 4703
Assignment: Lab II
Collaborators: Brianna Brost, Lucy Kien
Internet Source: ChatGPT (for leap year regex)
"""
#imports
import re
from nltk import PorterStemmer

#Part II: Using Regular Expressions in Python
def find_the(text: str):
    """
    Description of Function: This function searches for the word 'the' in a string
    Parameters: text: str -- the text to search for the word 'the'
    Return: list -- list of found words
    """
    words = re.findall(r'the', text)
    print('Number of "the" in the text:', words)

def find_hello (text: str):
    """
    Description of Function: This function searches for the first case-insensitive occurence of the word 'hello' in a string
    Parameters: text: str -- the text to search for the word 'hello'
    Return: int -- index of the first occurence of the word 'hello'
    """
    words = re.search(r'hello', text, re.IGNORECASE)
    print('First occurence of "hello" in the text:', words.start())

def find_digit(text: str):
    """
    Description of Function: This function searches for all the digits in a string
    Parameters: text: str -- the text to search for digits
    Return: list -- list of found digits
    """
    words = re.findall(r'\d', text)
    print('Digits in the text:', words)

def find_vowel_words(text: str):
    """
    Description of Function: This function searches for all the words that start with a vowel in a string
    Parameters: text: str -- the text to search for words that start with a vowel
    Return: list -- list of found words
    """
    words = re.findall(r'\b[aeiouAEIOU]\w*', text)
    print('Words that start with a vowel:', words)

def find_n_k(text: str, k: int):
    """
    Description of Function: This function searches for all the words that have the letter n repeated k times in a string
    Parameters: text: str -- the text to search for words that have the letter n repeated k times
                k: int -- the number of times the letter n is repeated
    Return: list -- list of found words
    """
    words = re.findall(r'\b\w*n\w*\b', text)
    result = [word for word in words if word.count('n') >= k]
    print('Words that have the letter n repeated', k, 'times:', result)

def match_start_end(text: str):
    """
    Description of Function: This function searches for all the words that start and end with the same letter in a string
    Parameters: text: str -- the text to search for words that start and end with the same letter
    Return: list -- list of found words
    """
    words = re.findall(r'\b(\w+(\w)\w*)\b', text.lower())
    result = [word[0] for word in words if word[1] == word[0][0]]
    print('Words that start and end with the same letter:', result)

def first_word_in_sentence(text: str):
    """
    Description of Function: This function searches for all the first words in each sentence in a string
    Parameters: text: str -- the text to search for the first words in each sentence
    Return: list -- list of found words
    """
    words = re.findall(r'\b[A-Z]\w*', text)
    print('First words in each sentence:', words)

def valid_date(date: str):
    """
    Description of Function: This function checks if a string is a valid date in the format YYYY-MM-DD
    Parameters: text: str -- the text to check if it is a valid date
    Return: bool -- True if the date is valid, False otherwise
    """
    # separate the date out
    year, month, day = map(int, re.split(r'[-/]', date))
    if len(str(year)) != 4:
        # more than 4 ints in year false
        return False
    if month < 1 or month > 12:
        # not within scope of months
        return False
    if day < 1:
        # negatives
        return False
    if month in {1, 3, 5, 7, 8, 10, 12}:
        # months with 31 days
        return day <= 31
    elif month in {4, 6, 9, 11}:
        # months with 30 days
        return day <= 30
    elif month == 2:
        # leap year function below
        if is_leap_year(year):
            return day <= 29
        else:
            return day <= 28
    else:
        return False

#leap year function used an LLM to figure this one out
def is_leap_year(year: str):
    """"
    Description of Helper Function: This function checks if a year is a leap year
    Parameters: year: str -- the year to check if it is a leap year
    Return: bool -- True if the year is a leap year, False otherwise
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def extract_domain(url: str):
    """
    Description of Function: This function extracts the domain name from a URL
    Parameters: url: str -- the URL to extract the domain name from
    Return: str -- the domain name
    """
    domain = re.search(r'(?<=://)([\w-]+\.)+[\w-]+', url)
    print('Domain name:', domain.group())

def remove_RT(text: str):
    """
    Description of Function: This function removes the 'RT' from a string only if it is at the beginning of the string
    Parameters: text: str -- the text to remove 'RT' from
    Return: str -- the text with 'RT' removed
    """
    result = re.sub(r'RT\s', '', text, flags = re.IGNORECASE)
    print('Text with RT removed:', result)

def extract_IP_addresses(text: str):
    """
    Description of Function: This function extracts all the IP addresses from a string
    Parameters: text: str -- the text to extract IP addresses from
    Return: list -- list of found IP addresses
    """
    # Regular expression pattern for matching IP addresses
    pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    
    # Find all matches in the text
    matches = re.findall(pattern, text)
    
    # Filter out invalid IP addresses
    valid_IPs = []
    for match in matches:
        parts = match.split('.')
        if len(parts) == 4:
            valid = True
            for part in parts:
                if not 0 <= int(part) <= 255:
                    valid = False
                    break
            if valid:
                valid_IPs.append(match)
    
    return valid_IPs

def replace_color(text: str):
    """
    Description of Function: This function replaces every instance of the word 'color' with 'colour' in a string
    Parameters: text: str -- the text to replace 'color' with 'colour'
    Return: str -- the text with 'color' replaced with 'colour'
    """
    words = re.sub(r'\bcolor\b', 'colour', text)
    print('Text with color replaced with colour:', words)

#Part III: Stemming

#creating the stemmer object
stemmer = PorterStemmer()

def stem_words(words):
    """
    Description of Function: This function stems a list of words
    Parameters: words: list -- the list of words to stem
    Return: list -- the list of stemmed words
    """
    stemmed = []
    for word in words:
        stemmed.append(stemmer.stem(word))
    return stemmed

#driver code
def main():
    print('Part II: Using Regular Expressions in Python')
    print('I:')
    find_the('the cat in the hat')
    print('\nII:')
    find_hello('theHELLohi')
    print('\nIII:')
    find_digit('I am 25 years old')
    print('\nIV:')
    find_vowel_words('I am 25 years old')
    print('\nV:')
    find_n_k('manners yoink', 1)
    print('\nVI:')
    match_start_end('The eve of tent seeds')
    print('\nVII:')
    first_word_in_sentence('I am 25 years old. But my brother is 10 years younger.')
    print('\nVIII:')
    print("Is '2021-12-01' a valid date?", valid_date('2021-12-01'))
    print("Is '2021-13-01' a valid date?", valid_date('2021-13-01'))
    print("Is '2021-12-32' a valid date?", valid_date('2021-12-32'))
    print("Is '2021-02-29' a valid date?", valid_date('2021-02-29'))
    print("Is '2020-02-29' a valid date?", valid_date('2020-02-29'))
    print('\nIX:')
    extract_domain('https://canvas.du.edu/courses/')
    print('\nX:')
    remove_RT('RT hello')
    remove_RT('hello RT')
    print('\nXI:')
    text = "192.168.1.1, 256.0.0.1, 3.22.214.0, 999.999.999.999, and 127.0.0.1"
    print("Here are the valid IP addresses:", (extract_IP_addresses(text)))
    print('\nXII:')
    replace_color('I love the color colorful red')
    print('\nPart III: Stemming')
    print('I:')
    words = [ "happy", "finally", "continue", "friendly", "biology", "value", "likely"]
    print(stem_words(words))

if __name__ == '__main__':
    main()