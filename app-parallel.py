import utils
import multiprocessing

URL_REGEX = r'href="(\/\S*?.epi)"'

def scrape_category(category):
    posts_date = []
    posts_content = []
    posts_unique_url = []

    for page_num in range(1, 10):
        category_url = f"https://baomoi.com/{category}/trang{page_num}.epi"
        html = utils.getPageResponse(category_url)
        posts_url = utils.getURLFromPage(html, URL_REGEX)

        for url in posts_url:
            body, date = utils.getPageContent(url)
            posts_content.append(body)
            posts_date.append(date)

        for content in posts_content:
            posts_unique_url.append(utils.urlRegex(content))

    jsonData = utils.jsonFormatter(posts_unique_url, posts_content, posts_date)
    utils.writeFile(f"{category}.json", jsonData)

if __name__ == "__main__":
    categories = ["giao-duc", "khoa-hoc", "giai-tri", "kinh-te"]

    # Create a process pool with 4 workers
    pool = multiprocessing.Pool(processes=4)

    # Map the scrape_category function to each category in parallel
    pool.map(scrape_category, categories)

    # Close the pool to free up resources
    pool.close()
    pool.join()
