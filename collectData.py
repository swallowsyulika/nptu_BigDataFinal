import requests
from bs4 import BeautifulSoup
import os


def download_image(img_url: str, name: str):
    with open(name, 'wb') as handle:
        response = requests.get(img_url, stream=True)
        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)

index = 0
runs = 2
countPath = "customData/count.txt"
savePath = "customData"
imgsUrl = "https://safebooru.org/index.php?page=post&s=list&tags=front-tie_top+&pid="
Purl = "https://safebooru.org/"


for i in range(runs):
    r = requests.get(imgsUrl + f"{40 * i}")
    soup = BeautifulSoup(r.text, "lxml")
    imgList = soup.find_all(class_="preview")
    imgPaths = [x.parent.get("href") for x in imgList]
    
    for imgPath in imgPaths:
        url = Purl + imgPath
        ir = requests.get(url)
        isoup = BeautifulSoup(ir.text, "lxml")
        src = isoup.find(id="image").get("src")

        with open(countPath) as f:
            index = int(f.readline().strip())

        print("Download: ", src)
        try:
            download_image(src, os.path.join(savePath, f"image_{str(index).zfill(4)}.jpg"))
            index += 1
        except:
            print("Above image download failed.")

        with open(countPath, "w") as f:
            f.write(str(index))

