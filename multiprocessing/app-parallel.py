import sys
# setting path
sys.path.append('../regex-scrapper/')

import multiprocessing
from utils import getPageResponse, getURLFromPage, getPageContent, urlRegex, jsonFormatter, writeFile

URL_REGEX = r'href="(\/\S*?.epi)"'

def scrape_category(category):
    posts_date = []
    posts_content = []
    posts_unique_url = []

    category_url = f"https://baomoi.com/{category}.epi"
    html = getPageResponse(category_url)
    posts_url = getURLFromPage(html, URL_REGEX)

    for url in posts_url:
        body, date = getPageContent(url)
        posts_content.append(body)
        posts_date.append(date)

    for content in posts_content:
        posts_unique_url.append(urlRegex(content))

    jsonData = jsonFormatter(posts_unique_url, posts_content, posts_date)
    writeFile(f"./multiprocessing/output/{category}.json", jsonData)

if __name__ == "__main__":
    categories = ["giao-duc", "khoa-hoc-cong-nghe", "khoa-hoc", "giai-tri", "kinh-te", "nha-dat"]

    # Create a process pool with 6 workers
    pool = multiprocessing.Pool(processes=6)

    # Map the scrape_category function to each category in parallel
    pool.map(scrape_category, categories)

    # Close the pool to free up resources
    pool.close()
    pool.join()
