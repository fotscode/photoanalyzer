import os
import bs4
import urllib.request
import random
import pytesseract as tess
tess.pytesseract.tesseract_cmd=r"C:\Users\cacut\AppData\Local\Tesseract-OCR\tesseract.exe"
from PIL import Image

def wordcount(file,listwords,code,filename):         
        line=file.split()
        count=0
        for word in listwords:
            lower=word.lower()
            for sentence in line:
                line2=sentence.lower()
                if lower == line2:
                        count+=1
        if count > 0:
                newName="imageswithkeywords/"+code+".png"
                os.rename(filename,newName)
                print("One or more of the keywords was found!")
        else:
                os.remove(filename)
                print("Keywords weren't found")

def linkImg(url):
    r = urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36'})
    htmlf = urllib.request.urlopen(r)
    subhtml = htmlf.read()
    soup = bs4.BeautifulSoup(subhtml,features="lxml")
    images = soup.findAll('img')
    for image in images:
        name = image['src']
        break 
    return name

lettersandnumbers = ["0","1","2","3","4","5","6","7","8","9","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]          


while True:
    sixdigitcode = random.choices(lettersandnumbers, k=6)
    linkprnt="https://prnt.sc/"
    code=("".join(sixdigitcode))
    finalink=linkprnt+code
    print(finalink) 
    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener) 
    filename = 'temporaryfile.png'
    link = linkImg(finalink)
    if 'https:' not in link:
            print("Screenshot wasn't found")
            continue
    urllib.request.urlretrieve(link, filename)
    img = Image.open(filename).convert("RGB")
    text = tess.image_to_string(img)
    wordcount(text,["keyword1","keyword2","keyword3"],code,filename)

