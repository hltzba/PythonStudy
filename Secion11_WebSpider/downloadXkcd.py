# encoding:utf-8
#! python3
# downloadXkcd.py - Download every single XKCD comic.
import requests,bs4,os
url='https://xkcd.com/'
savedir='C:\\XKCD'
os.makedirs(savedir,exist_ok=True)
while not url.endswith('#'):
    # TODO:Download the page.
    print('Downloading page %s...'%url)
    res=requests.get(url)
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text,features="html.parser")
    # TODO:Find the url of the comic image.
    comicElem=soup.select('#comic img')
    if comicElem==[]:
        print('Could not find comic image.')
    else:
        comicUrl='https:'+comicElem[0].get('src')
        # TODO:Downloading image.
        print('Downloading image %s...'%comicUrl)
        res=requests.get(comicUrl)
        res.raise_for_status()
        # TODO:Save the image to disk.
        imageFile=open(os.path.join(savedir,os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(1000000):
            imageFile.write(chunk)
        imageFile.close()     
    # TODO:Get prev button's url.
    prevLink=soup.select('a[rel="prev"]')[0]
    url='https://xkcd.com'+prevLink.get('href')
print('Done.')