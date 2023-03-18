import utils 

URL_REGEX = r'href="(\/\S*?.epi)"'
CATEGORY = "https://baomoi.com/khoa-hoc/trang1.epi/"

pagination = list(range(1, 10))

html = utils.getPageResponse(CATEGORY)
posts_url = utils.getURLFromPage(html, URL_REGEX)

for url in posts_url:
    print(url)