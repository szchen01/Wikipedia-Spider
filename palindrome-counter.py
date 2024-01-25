import requests
from bs4 import BeautifulSoup

# count the number of palindromes in the body of a given wikipedia article


def palindrome_counter(url):
    response = requests.get(
        url=url,
    )

    soup = BeautifulSoup(response.content, 'html.parser')

    # mw-content-text is the id for the div tag that contains the main content of an article
    allContent = soup.find(id="mw-content-text").stripped_strings
    allLines = [text for text in allContent]
    allWords = []
    for line in allLines:
        allWords.extend(line.split())

    count = 0
    palindromes = []

    def isPalindrome(word):
        return word == word[::-1] and len(word) >= 3 and word.isalpha()
    for word in allWords:
        if isPalindrome(word):
            count += 1
            if not word in palindromes:
                palindromes.append(word)
    print(f'There are {count} palindromes in this article:')
    print(palindromes)
    return count, palindromes


palindrome_counter(
    "https://en.wikipedia.org/wiki/Palindrome")
