# It will download image in hd

import requests
from bs4 import BeautifulSoup as soup

if __name__ == '__main__':
    uname = str(input("Enter the username : "))
    new = requests.get(f'https://www.instadp.com/fullsize/{uname}')
    imgsoup = soup(new.content, 'lxml')
    imglink = imgsoup.find('img', {'class': 'picture'})['src']
    imgfind = requests.get(imglink)
    with open('photo.png', 'wb') as photo:
        photo.write(imgfind.content)
