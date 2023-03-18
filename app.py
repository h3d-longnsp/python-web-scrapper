import utils 

URL_REGEX = r'href="(\/\S*?.epi)"'
CATEGORY = "https://baomoi.com/khoa-hoc/trang1.epi/"

posts_date       = []
posts_content    = []
posts_unique_url = []

pagination = list(range(1, 10))

html = utils.getPageResponse(CATEGORY)
posts_url = utils.getURLFromPage(html, URL_REGEX)

for url in posts_url:
    body, date = utils.getPageContent(url)
    posts_content.append(body)
    posts_date.append(date)

for content in posts_content:
    posts_unique_url.append(utils.urlRegex(content))

jsonData = utils.jsonFormatter(posts_unique_url, posts_content, posts_date)

utils.writeFile("NguyenSyPhiLong.json", jsonData)