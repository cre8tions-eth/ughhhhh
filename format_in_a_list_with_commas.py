import requests
from bs4 import BeautifulSoup

def get_bad_words(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return [word.text for word in soup.find('ul', {'id': 'words'}).find_all('li')]

bad_words = get_bad_words("https://www.freewebheaders.com/full-list-of-bad-words-banned-by-google/")
bad_words_str = ', '.join(bad_words)

print(f"The list of bad words from 'https://www.freewebheaders.com/full-list-of-bad-words-banned-by-google/' is:\n{bad_words_str}")
```python
import requests
from bs4 import BeautifulSoup

# The function to scrape the words from a url
def get_bad_words(url):
    # Make a GET request to retrieve the HTML of "The Big List of Bad Words" website.
    r = requests.get(url)

    # Create a Beautiful Soup object from the HTML.
    soup = BeautifulSoup(r.text, 'html.parser')

    # Find all <li> tags within the <ul id="words"> tag on the page and get their text.
    bad_word_list = [word.text for word in soup.find('ul', {'id': 'words'}).find_all('li')]

    return bad_word_list
```


```python
bad_words =
get_bad_words("https://www.freewebheaders.com/full-list-of-bad-words-banned-by-google/")
bad_words_str = ', '.join(bad_words)

print(f"The list of bad words from
'https://www.freewebheaders.com/full-list-of-bad-words-banned-by-google/'
is:\n{bad_words_str}")
```
