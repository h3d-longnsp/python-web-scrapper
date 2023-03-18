import re
import json
import requests
from functools import reduce
from collections import OrderedDict
from bs4 import BeautifulSoup, ResultSet

HOMEPAGE = "https://baomoi.com"
UNIQUE_URL_REGEX = r"\b(https|http):\/\/\S+\b"
    
def concatStrings(a: str, b: str):
    return a + " " + b

def getText(body: ResultSet):
    return reduce(concatStrings, map(lambda n: n.text, body))

def getPageResponse(url: str) -> str:
    """ Sends an HTTP GET request to the specified URL and 
    returns the response content as a string.

    Args:
        `url` (str): The URL to which the request is sent.

    Returns:
        `response` (str): The response content as a string, decoded 
        using the UTF-8 encoding.
    """
    response = requests.get(url)
    return response.content.decode('utf-8')

def getURLFromPage(pageHtml: str, pattern: str) -> list[str]:
    """ Extracts URLs from a webpage HTML content based on the specified pattern, 
    and returns a list of unique URLs filtered by length.

    Args:
        `pageHtml` (str): The HTML content of the webpage as a string.
        `pattern` (str): The regex pattern to use.

    Returns:
        list[str]: List of unique URLs extracted where each URL 
        is a string in the form of HOMEPAGE+url.
    """
    match = re.findall(pattern, pageHtml)
    # use OrderedDict and not Set to preserve the order of appearance
    unique_urls = list(OrderedDict.fromkeys(match))
    return [HOMEPAGE + url for url in unique_urls if len(url) > 40]

def getPageContent(url: str) -> tuple[str, str]:
    """ Retrieves the HTML content of a webpage using the provided URL, extracts the text from 
    the heading tag and all paragraph tags in the HTML, and returns a tuple containing the text 
    and the `datetime` attribute of the first time tag found in the HTML.

    Args:
        `url` (str): The URL of the webpage to retrieve.

    Returns:
        tuple[str, str]: A tuple containing two strings:
        
        - The concatenated text of the heading and all paragraph tags in the HTML content.
        - The value of the datetime attribute of the first time tag found in the HTML content.
        If no paragraphs are found in the HTML content, an empty string is returned for both values.
    """
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    heading = soup.find('h3')
    paragraphs = soup.find_all("p")
    time = soup.find("time")
    return (heading.text + " " + getText(paragraphs), time.get("datetime")) if paragraphs else ("", "")
    
def urlRegex(source: str) -> str:
    """ Using regex to extract source url
    
    When a string matches the pattern, `re.search()` returns a match object. 
    To get only the matched part as a string, using `group()` method of 
    the match object.
    
    Args:
        `source` (str): The string to search for the unique URL pattern..
        
    Returns:
        `source_url` (str): Source url of the post, or an empty string if no
        pattern is found.
    """
    try:
        url = re.search(UNIQUE_URL_REGEX, source).group()
        return url
    except AttributeError:
        return ""

def jsonFormatter(url: list, content: list, date: list):
    """ Formats the provided lists of URL, content, and date strings into a list of dictionaries
    suitable for conversion to JSON. Filters out any tuples where any of the elements are empty strings.

    Args:
        `url` (list): A list of URL strings.
        `content` (list): A list of content strings.
        `date` (list): A list of date strings.

    Returns:
        list[dict]: A list of dictionaries, each dictionary has three keys:
        - `url`: The URL string from the corresponding index of the `url` list.
        - `content`: The content string from the corresponding index of the `content` list.
        - `date`: The date string from the corresponding index of the `date` list.
    """
    keys = ["url", "content", "date"] 
    tmp = list(zip(url, content, date))
    inp = [tpl for tpl in tmp if not any(x == "" for x in tpl)]
    output = [dict(zip(keys, elem)) for elem in inp]
          
    return output

def writeFile(filename: str, data: list[dict]):
    """ Write json-formatted data to `*.json` file.
     
    Set `ensure_ascii`=`False` to make `json.dump` leave encoding to file object.

    Args:
        `filename` (str): path to filename
        `data` (list[dict]): json-formatted data
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"{filename} created!")
        
    f.close
    