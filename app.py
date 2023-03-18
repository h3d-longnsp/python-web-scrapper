import utils 
import argparse

URL_REGEX = r'href="(\/\S*?.epi)"'

posts_date       = []
posts_content    = []
posts_unique_url = []

def parser():
    parser = argparse.ArgumentParser(description='Python web scrapper.')
    parser.add_argument("-c", "--category", help="Category to scrape.", default="khoa-hoc")
    return parser.parse_args()    

def main():
    args = parser()
    category_url = f"https://baomoi.com/{args.category}.epi"
    html = utils.getPageResponse(category_url)
    posts_url = utils.getURLFromPage(html, URL_REGEX)

    for url in posts_url:
        body, date = utils.getPageContent(url)
        posts_content.append(body)
        posts_date.append(date)

    for content in posts_content:
        posts_unique_url.append(utils.urlRegex(content))

    jsonData = utils.jsonFormatter(posts_unique_url, posts_content, posts_date)

    utils.writeFile(f"NSPL-{args.category}.json", jsonData) 

if __name__ == "__main__":
    main()