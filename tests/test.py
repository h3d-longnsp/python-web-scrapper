from bs4 import BeautifulSoup
import requests
import utils

url = "https://baomoi.com/phat-hien-hoa-chat-vinh-cuu-trong-giay-ve-sinh/c/45316395.epi"
url2= "https://baomoi.com/chuyen-trang-hoa-hoc-tro-bao-tien-phong/p/105.epi"
SCIENCE = "https://baomoi.com/khoa-hoc.epi/"

url3 = "https://baomoi.com/chuyen-trang-an-ninh-thu-do-bao-cong-an-nhan-dan/p/106.epi"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.prettify())

body, date = utils.getPageContent(url2)

print(body)

print(date)


a = utils.urlRegex("")