import requests
from bs4 import BeautifulSoup
import pdb

album_url = 'https://www.douban.com/photos/album/156951271/'
cookie_file = 'cookie.txt'

with open(cookie_file, 'rb') as 




start = 0
while True:
    target_album = album_url + '?start=%d'%(start)
    pdb.set_trace()
    r = requests.get(target_album)
    soup = BeautifulSoup(r.text, 'html.parser')
    divs = soup.find_all('div')
    img_candidates = []
    for div in divs:
        if div.has_attr('class') and 'photo_wrap' in div['class']:
            img_candidates.append(div.a.img['src'])
    if len(img_candidates) == 0:
        break

    for url in img_candidates:
        img_filename = url.split('/')[-1]
        large_photo = "http://img3.doubanio.com/view/photo/photo/public/%s"%(img_filename)
        response = requests.get(large_photo, stream = True)
        if not response.ok:
            #something went wrong
            pass
        handle = open(img_filename, 'wb')
        for block in response.iter_content(1024):#chuck size
            handle.write(block)
    start += len(img_candidates)
    
            #download the image
            #del_request = requests.get('http://douban.com/%d/delete'%(img_id))

#for image in image_folder:
#()    %upload it
