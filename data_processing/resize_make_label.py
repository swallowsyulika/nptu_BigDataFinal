import xml.etree.ElementTree as ET
import os
import cv2

Ann_path = "Annotations"
Ani_path = "JPEGImages"
img_path = "images"
lb_path = "labels"
imageSize = 480

save_image = True
save_label = True


def resize_and_save(Ann_path: str, Ani_path: str, img_path: str, lb_path: str, imgSize: int):
    tree = ET.parse(Ann_path)
    root = tree.getroot()

    imgName = root.find("filename").text
    BBox = []

    for neighbor in root.iter("bndbox"):
        xmin = int(neighbor.find('xmin').text)
        ymin = int(neighbor.find('ymin').text)
        xmax = int(neighbor.find('xmax').text)
        ymax = int(neighbor.find('ymax').text)

        BBox.append([xmin, ymin, xmax, ymax])

    # resize and save image
    img = cv2.imread(os.path.join(Ani_path, imgName))
    rimg = cv2.resize(img, dsize=(imgSize, imgSize), interpolation=cv2.INTER_CUBIC)
    if save_image:
        cv2.imwrite(os.path.join(img_path, imgName), rimg)
    
    if save_label:
        with open(os.path.join(lb_path, imgName.replace("jpg", "txt")), "w") as fp:
            for ele in BBox:
                # resize BBox
                w_ratio = imgSize / img.shape[0]
                h_ratio = imgSize / img.shape[1]
                ratioList = [h_ratio, w_ratio, h_ratio, w_ratio]

                box = [int(a * b) for a, b in zip(ele, ratioList)]

                # box xmin, ymin, xmax, ymax
                xc = ((box[0]+box[2])//2) / imgSize
                yc = ((box[1]+box[3])//2) / imgSize
                w = (box[2] - box[0]) / imgSize
                h = (box[3] - box[1]) / imgSize
                ybox = [xc, yc, w, h]
                # save labels
                s = [str(x) for x in ybox]
                fp.write("1 ")
                fp.write(" ".join(s))
                fp.write("\n")

annotations = os.listdir(Ann_path)
for annotation in annotations:
    resize_and_save(os.path.join(Ann_path, annotation), Ani_path, img_path, lb_path, imageSize)
        
    